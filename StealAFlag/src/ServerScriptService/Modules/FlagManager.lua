--[[
	FlagManager
	Builds the two flags and runs every flag rule: stealing, carrying, dropping,
	returning and capturing. Flag positions are checked a few times a second
	with distance tests instead of Touched events, which is far more reliable.
]]

local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local Workspace = game:GetService("Workspace")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))
local GameState = require(script.Parent:WaitForChild("GameState"))
local TeamManager = require(script.Parent:WaitForChild("TeamManager"))

local FlagManager = {}
FlagManager.Flags = {}
FlagManager.Enabled = false
FlagManager.OnCapture = nil -- callback(scoringTeamIndex, player), set by RoundManager

local POLE_HEIGHT = 9
local BANNER_WIDTH = 5
local BANNER_HEIGHT = 3.5
local TICK_INTERVAL = 0.1

local flagsFolder = nil

-- The pole is a cylinder, whose long axis is its local X. Rotating it 90 degrees
-- around Z stands it upright, so "up the pole" is +X in the pole's local space.
local function poleCFrameAt(groundPosition)
	return CFrame.new(groundPosition + Vector3.new(0, POLE_HEIGHT / 2, 0)) * CFrame.Angles(0, 0, math.rad(90))
end

local function weldTo(part, base)
	local weld = Instance.new("WeldConstraint")
	weld.Part0 = base
	weld.Part1 = part
	weld.Parent = part
end

local function addStat(player, statName, amount)
	local stats = player:FindFirstChild("leaderstats")
	local stat = stats and stats:FindFirstChild(statName)
	if stat then
		stat.Value += amount
	end
end

local function buildFlag(index, def, groundPosition)
	local model = Instance.new("Model")
	model.Name = def.Name .. " Flag"

	local pole = Instance.new("Part")
	pole.Name = "Pole"
	pole.Shape = Enum.PartType.Cylinder
	pole.Size = Vector3.new(POLE_HEIGHT, 0.5, 0.5)
	pole.Color = Color3.fromRGB(225, 225, 225)
	pole.Material = Enum.Material.Metal
	pole.Anchored = true
	pole.CanCollide = false
	pole.CFrame = poleCFrameAt(groundPosition)
	pole.Parent = model
	model.PrimaryPart = pole

	local parts = { pole }

	-- banner: one stripe per team colour, stacked from the top of the pole down
	local stripeHeight = BANNER_HEIGHT / #def.Colors
	for i, color in ipairs(def.Colors) do
		local stripe = Instance.new("Part")
		stripe.Name = "Stripe" .. i
		stripe.Size = Vector3.new(stripeHeight, 0.2, BANNER_WIDTH)
		stripe.CFrame = pole.CFrame * CFrame.new(POLE_HEIGHT / 2 - 0.4 - stripeHeight * (i - 0.5), 0, BANNER_WIDTH / 2 + 0.25)
		stripe.Color = color
		stripe.Material = Enum.Material.SmoothPlastic
		stripe.Anchored = true
		stripe.CanCollide = false
		stripe.Parent = model
		weldTo(stripe, pole)
		table.insert(parts, stripe)
	end

	-- glowing orb on top so the flag is easy to spot from far away
	local orb = Instance.new("Part")
	orb.Name = "Orb"
	orb.Shape = Enum.PartType.Ball
	orb.Size = Vector3.new(1.3, 1.3, 1.3)
	orb.CFrame = pole.CFrame * CFrame.new(POLE_HEIGHT / 2 + 0.4, 0, 0)
	orb.Color = def.Colors[1]
	orb.Material = Enum.Material.Neon
	orb.Anchored = true
	orb.CanCollide = false
	orb.Parent = model
	weldTo(orb, pole)
	table.insert(parts, orb)

	local light = Instance.new("PointLight")
	light.Color = def.Colors[1]
	light.Range = 14
	light.Brightness = 2
	light.Parent = orb

	local offsets = {}
	for _, part in ipairs(parts) do
		part.CanQuery = false -- flags never block shots or mouse aim
		part.CanTouch = false
		part.Massless = true
		if part ~= pole then
			offsets[part] = pole.CFrame:ToObjectSpace(part.CFrame)
		end
	end

	model.Parent = flagsFolder

	return {
		Index = index,
		Model = model,
		Pole = pole,
		Parts = parts,
		Offsets = offsets,
		HomeCFrame = pole.CFrame,
		HomePosition = groundPosition,
		GroundPosition = groundPosition,
		State = "Home",
		Carrier = nil,
		Weld = nil,
		DropTime = 0,
		LastCarrierPosition = nil,
	}
end

-- Re-aligns every banner part to the pole, so the flag always looks right after teleporting it.
local function snapParts(flag)
	for part, offset in pairs(flag.Offsets) do
		part.CFrame = flag.Pole.CFrame * offset
	end
end

local function setAnchored(flag, anchored)
	for _, part in ipairs(flag.Parts) do
		part.Anchored = anchored
	end
end

local function setState(flag, state, carrierName)
	flag.State = state
	GameState.Set("Flag" .. flag.Index .. "State", state)
	GameState.Set("Flag" .. flag.Index .. "Carrier", carrierName or "")
end

local function clearCarrier(flag)
	if flag.Weld then
		flag.Weld:Destroy()
		flag.Weld = nil
	end
	local carrier = flag.Carrier
	flag.Carrier = nil
	if carrier then
		carrier:SetAttribute("CarryingFlag", nil)
		local character = carrier.Character
		local humanoid = character and character:FindFirstChildOfClass("Humanoid")
		if humanoid and humanoid.Health > 0 then
			humanoid.WalkSpeed = Config.WalkSpeed
		end
	end
end

local function getAliveRoot(player)
	local character = player.Character
	if not character then
		return nil
	end
	local humanoid = character:FindFirstChildOfClass("Humanoid")
	if not humanoid or humanoid.Health <= 0 then
		return nil
	end
	return character:FindFirstChild("HumanoidRootPart")
end

local function withinReach(root, groundPosition, radius)
	local offset = root.Position - groundPosition
	local horizontal = Vector3.new(offset.X, 0, offset.Z).Magnitude
	return horizontal <= radius and math.abs(offset.Y) <= 8
end

function FlagManager.ReturnHome(flag)
	clearCarrier(flag)
	setAnchored(flag, true)
	flag.Pole.CFrame = flag.HomeCFrame
	snapParts(flag)
	flag.GroundPosition = flag.HomePosition
	setState(flag, "Home")
end

function FlagManager.Pickup(flag, player)
	local character = player.Character
	if not character then
		return
	end
	local humanoid = character:FindFirstChildOfClass("Humanoid")
	if not humanoid or humanoid.Health <= 0 then
		return
	end
	local torso = character:FindFirstChild("UpperTorso")
		or character:FindFirstChild("Torso")
		or character:FindFirstChild("HumanoidRootPart")
	if not torso then
		return
	end

	clearCarrier(flag)

	-- Position the pole on the carrier's back while still anchored, weld it, then let it move.
	setAnchored(flag, true)
	flag.Pole.CFrame = torso.CFrame
		* CFrame.new(0, 0.8, 0.9)
		* CFrame.Angles(math.rad(-20), 0, 0)
		* CFrame.Angles(0, 0, math.rad(90))
	snapParts(flag)

	local weld = Instance.new("WeldConstraint")
	weld.Name = "CarryWeld"
	weld.Part0 = torso
	weld.Part1 = flag.Pole
	weld.Parent = flag.Pole
	flag.Weld = weld
	setAnchored(flag, false)

	flag.Carrier = player
	flag.LastCarrierPosition = torso.Position
	player:SetAttribute("CarryingFlag", flag.Index)
	humanoid.WalkSpeed = Config.FlagCarrierWalkSpeed
	setState(flag, "Carried", player.Name)

	local def = Config.Teams[flag.Index]
	GameState.Broadcast(player.Name .. " stole the " .. def.Name .. " flag!", def.Colors[1], 3, "pickup")
end

function FlagManager.Drop(flag, position)
	local carrierCharacter = flag.Carrier and flag.Carrier.Character
	clearCarrier(flag)
	setAnchored(flag, true)

	local map = Config.Map
	local margin = 6
	local x = math.clamp(position.X, -map.Length / 2 + margin, map.Length / 2 - margin)
	local z = math.clamp(position.Z, -map.Width / 2 + margin, map.Width / 2 - margin)

	-- find the ground under the drop point so the flag sits on whatever the carrier stood on
	local exclude = { flagsFolder }
	for _, player in ipairs(Players:GetPlayers()) do
		if player.Character then
			table.insert(exclude, player.Character)
		end
	end
	if carrierCharacter then
		table.insert(exclude, carrierCharacter)
	end
	local params = RaycastParams.new()
	params.FilterType = Enum.RaycastFilterType.Exclude
	params.FilterDescendantsInstances = exclude
	local result = Workspace:Raycast(Vector3.new(x, position.Y + 2, z), Vector3.new(0, -80, 0), params)
	local groundY = result and result.Position.Y or 0
	local ground = Vector3.new(x, groundY, z)

	flag.Pole.CFrame = poleCFrameAt(ground)
	snapParts(flag)
	flag.GroundPosition = ground
	flag.DropTime = os.clock()
	setState(flag, "Dropped")

	local def = Config.Teams[flag.Index]
	GameState.Broadcast("The " .. def.Name .. " flag was dropped!", def.Colors[1], 3, "drop")
end

local function capture(flag, player)
	local scoringIndex = TeamManager.GetIndex(player)
	if not scoringIndex then
		return
	end
	local def = Config.Teams[flag.Index]
	local scoringDef = Config.Teams[scoringIndex]

	FlagManager.ReturnHome(flag)
	addStat(player, "Captures", 1)
	GameState.Broadcast(
		player.Name .. " captured the " .. def.Name .. " flag for " .. scoringDef.Name .. "!",
		scoringDef.Colors[1],
		4,
		"capture"
	)
	if FlagManager.OnCapture then
		FlagManager.OnCapture(scoringIndex, player)
	end
end

function FlagManager.Tick()
	local now = os.clock()

	for _, flag in ipairs(FlagManager.Flags) do
		local def = Config.Teams[flag.Index]

		if flag.State == "Carried" then
			local carrier = flag.Carrier
			local root = carrier and carrier.Parent == Players and getAliveRoot(carrier)
			if not root then
				FlagManager.Drop(flag, flag.LastCarrierPosition or flag.HomePosition)
			else
				flag.LastCarrierPosition = root.Position
				local carrierIndex = TeamManager.GetIndex(carrier)
				if carrierIndex == nil or carrierIndex == flag.Index then
					-- carrier switched teams while holding it
					FlagManager.Drop(flag, root.Position)
				elseif FlagManager.Enabled then
					local ownFlag = FlagManager.Flags[carrierIndex]
					local ownFlagReady = (not Config.RequireOwnFlagHome) or ownFlag.State == "Home"
					if ownFlagReady and withinReach(root, ownFlag.HomePosition, Config.CaptureRadius) then
						capture(flag, carrier)
					end
				end
			end
		elseif flag.State == "Dropped" and now - flag.DropTime >= Config.FlagReturnTime then
			FlagManager.ReturnHome(flag)
			GameState.Broadcast("The " .. def.Name .. " flag returned to base.", def.Colors[1], 3, "return")
		end

		if FlagManager.Enabled and (flag.State == "Home" or flag.State == "Dropped") then
			for _, player in ipairs(Players:GetPlayers()) do
				local root = getAliveRoot(player)
				if root and withinReach(root, flag.GroundPosition, Config.PickupRadius) then
					local teamIndex = TeamManager.GetIndex(player)
					if teamIndex == flag.Index then
						if flag.State == "Dropped" then
							FlagManager.ReturnHome(flag)
							addStat(player, "Returns", 1)
							GameState.Broadcast(player.Name .. " returned the " .. def.Name .. " flag!", def.Colors[1], 3, "return")
							break
						end
					elseif teamIndex ~= nil and player:GetAttribute("CarryingFlag") == nil then
						FlagManager.Pickup(flag, player)
						break
					end
				end
			end
		end
	end
end

function FlagManager.OnPlayerDied(player)
	for _, flag in ipairs(FlagManager.Flags) do
		if flag.State == "Carried" and flag.Carrier == player then
			local character = player.Character
			local root = character and character:FindFirstChild("HumanoidRootPart")
			FlagManager.Drop(flag, (root and root.Position) or flag.LastCarrierPosition or flag.HomePosition)
		end
	end
end

function FlagManager.OnPlayerRemoving(player)
	FlagManager.OnPlayerDied(player)
end

function FlagManager.ResetAll()
	for _, flag in ipairs(FlagManager.Flags) do
		FlagManager.ReturnHome(flag)
	end
end

function FlagManager.SetEnabled(enabled)
	FlagManager.Enabled = enabled
end

function FlagManager.Init(map)
	flagsFolder = map.Folders.Flags
	for index, def in ipairs(Config.Teams) do
		local base = map.Bases[index]
		FlagManager.Flags[index] = buildFlag(index, def, base.FlagStandPosition)
	end

	local accumulator = 0
	RunService.Heartbeat:Connect(function(dt)
		accumulator += dt
		if accumulator < TICK_INTERVAL then
			return
		end
		accumulator = 0
		FlagManager.Tick()
	end)
end

return FlagManager
