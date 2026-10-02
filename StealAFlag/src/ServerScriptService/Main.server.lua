--[[
	Main
	Server entry point for Steal a Flag. Builds the map, sets up teams, flags,
	weapons and player stats, then starts the round loop.
]]

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))

local Modules = script.Parent:WaitForChild("Modules")
local MapBuilder = require(Modules:WaitForChild("MapBuilder"))
local TeamManager = require(Modules:WaitForChild("TeamManager"))
local FlagManager = require(Modules:WaitForChild("FlagManager"))
local CombatServer = require(Modules:WaitForChild("CombatServer"))
local RoundManager = require(Modules:WaitForChild("RoundManager"))

Players.RespawnTime = Config.RespawnTime

TeamManager.Init()
local map = MapBuilder.Build()
FlagManager.Init(map)
CombatServer.Init()

local function setupLeaderstats(player)
	if player:FindFirstChild("leaderstats") then
		return
	end
	local stats = Instance.new("Folder")
	stats.Name = "leaderstats"
	for _, statName in ipairs({ "Captures", "Kills", "Returns" }) do
		local value = Instance.new("IntValue")
		value.Name = statName
		value.Value = 0
		value.Parent = stats
	end
	stats.Parent = player
end

local function addTeamVisuals(player, character)
	local teamIndex = TeamManager.GetIndex(player)
	if not teamIndex then
		return
	end
	local color = Config.Teams[teamIndex].Colors[1]

	-- coloured outline so teams are obvious at a glance (hidden behind walls)
	local highlight = Instance.new("Highlight")
	highlight.Name = "TeamOutline"
	highlight.FillTransparency = 1
	highlight.OutlineColor = color
	highlight.OutlineTransparency = 0
	highlight.DepthMode = Enum.HighlightDepthMode.Occluded
	highlight.Parent = character

	-- team-coloured name tag that replaces the default one
	local head = character:FindFirstChild("Head")
	local humanoid = character:FindFirstChildOfClass("Humanoid")
	if head and humanoid then
		humanoid.DisplayDistanceType = Enum.HumanoidDisplayDistanceType.None

		local billboard = Instance.new("BillboardGui")
		billboard.Name = "NameTag"
		billboard.Adornee = head
		billboard.Size = UDim2.new(0, 200, 0, 40)
		billboard.StudsOffset = Vector3.new(0, 2.4, 0)
		billboard.MaxDistance = 140
		billboard.AlwaysOnTop = false
		billboard.PlayerToHideFrom = player

		local label = Instance.new("TextLabel")
		label.Size = UDim2.new(1, 0, 1, 0)
		label.BackgroundTransparency = 1
		label.Font = Enum.Font.GothamBold
		label.TextScaled = true
		label.Text = player.DisplayName
		label.TextColor3 = color
		label.TextStrokeTransparency = 0.3
		label.TextStrokeColor3 = Color3.new(0, 0, 0)
		label.Parent = billboard

		billboard.Parent = head
	end
end

local function onCharacterAdded(player, character)
	local humanoid = character:WaitForChild("Humanoid", 10)
	if not humanoid then
		return
	end
	humanoid.WalkSpeed = Config.WalkSpeed

	addTeamVisuals(player, character)
	task.spawn(CombatServer.TintWeapon, player)

	humanoid.Died:Once(function()
		FlagManager.OnPlayerDied(player)
		CombatServer.OnCharacterDied(player, humanoid)
	end)
end

local function onPlayerAdded(player)
	setupLeaderstats(player)
	TeamManager.AssignSmallest(player)

	player.CharacterAdded:Connect(function(character)
		onCharacterAdded(player, character)
	end)
	if player.Character then
		onCharacterAdded(player, player.Character)
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
for _, player in ipairs(Players:GetPlayers()) do
	onPlayerAdded(player)
end

Players.PlayerRemoving:Connect(function(player)
	FlagManager.OnPlayerRemoving(player)
	CombatServer.OnPlayerRemoving(player)
end)

RoundManager.Start()
print(string.format("[%s] server ready", Config.GameName))
