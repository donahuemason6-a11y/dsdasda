--[[
	CombatServer
	Hands out the Blaster and validates every shot on the server: cooldown, range,
	line of sight and friendly fire are all checked here, never on the client.
]]

local Players = game:GetService("Players")
local ServerStorage = game:GetService("ServerStorage")
local StarterPack = game:GetService("StarterPack")
local Workspace = game:GetService("Workspace")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))
local GameState = require(script.Parent:WaitForChild("GameState"))
local TeamManager = require(script.Parent:WaitForChild("TeamManager"))

local CombatServer = {}

local KILL_CREDIT_WINDOW = 6 -- seconds after a hit that a death still counts as a kill

local toolName = Config.Weapon.Name
local lastFire = {}

local function ensureHandle(tool)
	if tool:FindFirstChild("Handle") then
		return
	end
	local handle = Instance.new("Part")
	handle.Name = "Handle"
	handle.Size = Vector3.new(0.5, 0.9, 2.4)
	handle.Color = Color3.fromRGB(40, 40, 45)
	handle.Material = Enum.Material.Metal
	handle.CanCollide = false
	handle.Parent = tool
end

local function addStat(player, statName, amount)
	local stats = player:FindFirstChild("leaderstats")
	local stat = stats and stats:FindFirstChild(statName)
	if stat then
		stat.Value += amount
	end
end

local function onFire(player, targetPosition)
	if typeof(targetPosition) ~= "Vector3" then
		return
	end
	local character = player.Character
	if not character then
		return
	end
	local humanoid = character:FindFirstChildOfClass("Humanoid")
	if not humanoid or humanoid.Health <= 0 then
		return
	end
	local tool = character:FindFirstChild(toolName)
	if not tool or not tool:IsA("Tool") then
		return -- not equipped
	end

	local now = os.clock()
	local last = lastFire[player]
	if last and now - last < Config.Weapon.Cooldown * 0.9 then
		return
	end
	lastFire[player] = now

	local head = character:FindFirstChild("Head")
	if not head then
		return
	end
	local origin = head.Position
	local direction = targetPosition - origin
	if direction.Magnitude < 0.5 then
		return
	end
	direction = direction.Unit * Config.Weapon.Range

	local params = RaycastParams.new()
	params.FilterType = Enum.RaycastFilterType.Exclude
	params.FilterDescendantsInstances = { character }
	params.IgnoreWater = true
	local result = Workspace:Raycast(origin, direction, params)
	local endPosition = result and result.Position or (origin + direction)

	if result then
		local hitModel = result.Instance:FindFirstAncestorOfClass("Model")
		local victim = hitModel and Players:GetPlayerFromCharacter(hitModel)
		if victim and victim ~= player then
			local victimHumanoid = hitModel:FindFirstChildOfClass("Humanoid")
			if victimHumanoid and victimHumanoid.Health > 0 then
				if Config.Weapon.FriendlyFire or victim.Team ~= player.Team then
					victimHumanoid:SetAttribute("LastHitBy", player.UserId)
					victimHumanoid:SetAttribute("LastHitTime", os.clock())
					victimHumanoid:TakeDamage(Config.Weapon.Damage)
				end
			end
		end
	end

	local handle = tool:FindFirstChild("Handle")
	local visualOrigin = handle and handle.Position or origin
	local teamIndex = TeamManager.GetIndex(player)
	local color = teamIndex and Config.Teams[teamIndex].Colors[1] or Color3.new(1, 1, 1)
	GameState.WeaponFiredRemote:FireAllClients(visualOrigin, endPosition, color)
end

function CombatServer.Init()
	local template = ServerStorage:FindFirstChild(toolName) or StarterPack:FindFirstChild(toolName)
	if not template or not template:IsA("Tool") then
		warn("[Steal a Flag] No Tool named '" .. toolName .. "' found in ServerStorage; players will be unarmed.")
		return
	end
	ensureHandle(template)

	-- StarterPack hands the tool to every player on every spawn, no timing games needed.
	if not StarterPack:FindFirstChild(toolName) then
		local copy = template:Clone()
		copy.Parent = StarterPack
	end

	GameState.FireWeaponRemote.OnServerEvent:Connect(onFire)
end

-- Tints the player's blaster in their team colour. Purely cosmetic.
function CombatServer.TintWeapon(player)
	local teamIndex = TeamManager.GetIndex(player)
	if not teamIndex then
		return
	end
	local color = Config.Teams[teamIndex].Colors[1]
	local backpack = player:FindFirstChildOfClass("Backpack")
	local tool = (backpack and backpack:FindFirstChild(toolName))
		or (player.Character and player.Character:FindFirstChild(toolName))
	if not tool and backpack then
		tool = backpack:WaitForChild(toolName, 3)
	end
	local handle = tool and tool:FindFirstChild("Handle")
	if handle then
		handle.Color = color
	end
end

function CombatServer.OnCharacterDied(player, humanoid)
	local killerId = humanoid:GetAttribute("LastHitBy")
	local hitTime = humanoid:GetAttribute("LastHitTime")
	if not killerId or not hitTime or os.clock() - hitTime > KILL_CREDIT_WINDOW then
		return
	end
	local killer = Players:GetPlayerByUserId(killerId)
	if killer and killer ~= player then
		addStat(killer, "Kills", 1)
	end
end

function CombatServer.OnPlayerRemoving(player)
	lastFire[player] = nil
end

return CombatServer
