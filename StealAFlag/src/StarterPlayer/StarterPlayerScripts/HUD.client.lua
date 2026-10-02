--[[
	HUD
	Builds the on-screen interface from code: scores, round timer, flag status,
	announcements and the "you have the flag" warning. Reads everything from the
	GameState attributes the server replicates.
]]

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local TweenService = game:GetService("TweenService")
local SoundService = game:GetService("SoundService")

local player = Players.LocalPlayer
local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))
local state = ReplicatedStorage:WaitForChild("GameState")
local remotes = ReplicatedStorage:WaitForChild("Remotes")
local announceRemote = remotes:WaitForChild("Announce")
local playerGui = player:WaitForChild("PlayerGui")

local WHITE = Color3.new(1, 1, 1)
local PANEL = Color3.fromRGB(20, 20, 24)

local SOUNDS = {
	pickup = "rbxasset://sounds/snap.mp3",
	drop = "rbxasset://sounds/collide.wav",
	["return"] = "rbxasset://sounds/button.wav",
	capture = "rbxasset://sounds/victory.wav",
	win = "rbxasset://sounds/victory.wav",
	info = "rbxasset://sounds/electronicpingshort.wav",
}

local function makeLabel(parent, props)
	local label = Instance.new("TextLabel")
	label.BackgroundTransparency = 1
	label.Font = Enum.Font.GothamBold
	label.TextColor3 = WHITE
	label.TextScaled = true
	label.TextStrokeTransparency = 0.6
	label.Size = UDim2.new(1, 0, 1, 0)
	for key, value in pairs(props) do
		label[key] = value
	end
	label.Parent = parent
	return label
end

local function makeFrame(parent, props)
	local frame = Instance.new("Frame")
	frame.BackgroundColor3 = PANEL
	frame.BackgroundTransparency = 0.25
	frame.BorderSizePixel = 0
	for key, value in pairs(props) do
		frame[key] = value
	end
	local corner = Instance.new("UICorner")
	corner.CornerRadius = UDim.new(0, 8)
	corner.Parent = frame
	frame.Parent = parent
	return frame
end

local gui = Instance.new("ScreenGui")
gui.Name = "StealAFlagHUD"
gui.ResetOnSpawn = false
gui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling
gui.Parent = playerGui

-- Top bar: team 1 score | timer | team 2 score ---------------------------------
local topBar = Instance.new("Frame")
topBar.Name = "TopBar"
topBar.AnchorPoint = Vector2.new(0.5, 0)
topBar.Position = UDim2.new(0.5, 0, 0, 10)
topBar.Size = UDim2.new(0, 560, 0, 64)
topBar.BackgroundTransparency = 1
topBar.Parent = gui

local teamBoxes = {}
for index, def in ipairs(Config.Teams) do
	local box = makeFrame(topBar, {
		Name = "Team" .. index,
		Size = UDim2.new(0, 190, 1, 0),
		Position = (index == 1) and UDim2.new(0, 0, 0, 0) or UDim2.new(1, -190, 0, 0),
		BackgroundColor3 = def.Colors[1],
		BackgroundTransparency = 0.1,
	})
	makeLabel(box, {
		Name = "Title",
		Text = def.Name,
		Size = UDim2.new(1, -10, 0, 20),
		Position = UDim2.new(0, 5, 0, 4),
	})
	local score = makeLabel(box, {
		Name = "Score",
		Text = "0",
		Size = UDim2.new(1, -10, 0, 36),
		Position = UDim2.new(0, 5, 0, 24),
	})
	teamBoxes[index] = { Frame = box, Score = score }
end

local centreBox = makeFrame(topBar, {
	Name = "Centre",
	Size = UDim2.new(0, 170, 1, 0),
	Position = UDim2.new(0.5, -85, 0, 0),
})
local timerLabel = makeLabel(centreBox, {
	Name = "Timer",
	Text = "0:00",
	Size = UDim2.new(1, -10, 0, 36),
	Position = UDim2.new(0, 5, 0, 4),
})
local phaseLabel = makeLabel(centreBox, {
	Name = "Phase",
	Text = "",
	Size = UDim2.new(1, -10, 0, 18),
	Position = UDim2.new(0, 5, 0, 42),
	Font = Enum.Font.Gotham,
})

-- Status + flag lines under the top bar ------------------------------------------
local statusLabel = makeLabel(gui, {
	Name = "Status",
	Text = "",
	AnchorPoint = Vector2.new(0.5, 0),
	Position = UDim2.new(0.5, 0, 0, 80),
	Size = UDim2.new(0, 560, 0, 22),
	Font = Enum.Font.Gotham,
})

local flagLabels = {}
for index, def in ipairs(Config.Teams) do
	flagLabels[index] = makeLabel(gui, {
		Name = "Flag" .. index,
		Text = "",
		AnchorPoint = Vector2.new(0.5, 0),
		Position = UDim2.new(0.5, 0, 0, 104 + (index - 1) * 20),
		Size = UDim2.new(0, 560, 0, 18),
		Font = Enum.Font.Gotham,
		TextColor3 = def.Colors[1],
	})
end

-- Announcement in the middle of the screen ------------------------------------
local announceLabel = makeLabel(gui, {
	Name = "Announcement",
	Text = "",
	AnchorPoint = Vector2.new(0.5, 0.5),
	Position = UDim2.new(0.5, 0, 0.3, 0),
	Size = UDim2.new(0.8, 0, 0, 44),
	TextStrokeTransparency = 0.2,
	TextTransparency = 1,
})

-- Alert strip at the bottom (carrying the flag / your flag was stolen) ---------
local alertFrame = makeFrame(gui, {
	Name = "Alert",
	AnchorPoint = Vector2.new(0.5, 1),
	Position = UDim2.new(0.5, 0, 1, -24),
	Size = UDim2.new(0, 520, 0, 40),
	Visible = false,
})
local alertLabel = makeLabel(alertFrame, {
	Name = "Text",
	Text = "",
	Size = UDim2.new(1, -16, 1, -8),
	Position = UDim2.new(0, 8, 0, 4),
})

-- Controls hint that fades away after a while ---------------------------------
local hintLabel = makeLabel(gui, {
	Name = "Hint",
	Text = "Click to shoot. Walk into the enemy flag to steal it, then carry it back to your glowing ring.",
	AnchorPoint = Vector2.new(0.5, 1),
	Position = UDim2.new(0.5, 0, 1, -72),
	Size = UDim2.new(0, 640, 0, 20),
	Font = Enum.Font.Gotham,
})
task.delay(14, function()
	TweenService:Create(hintLabel, TweenInfo.new(1), { TextTransparency = 1, TextStrokeTransparency = 1 }):Play()
end)

-- Helpers ---------------------------------------------------------------------
local function myTeamIndex()
	local team = player.Team
	if not team then
		return nil
	end
	for index, def in ipairs(Config.Teams) do
		if team.Name == def.Name then
			return index
		end
	end
	return nil
end

local function formatTime(seconds)
	seconds = math.max(0, math.floor(tonumber(seconds) or 0))
	return string.format("%d:%02d", seconds // 60, seconds % 60)
end

local function playSound(kind)
	local id = SOUNDS[kind]
	if not id then
		return
	end
	local sound = Instance.new("Sound")
	sound.SoundId = id
	sound.Volume = 0.6
	SoundService:PlayLocalSound(sound)
	task.delay(4, function()
		sound:Destroy()
	end)
end

local function refresh()
	local phase = state:GetAttribute("Phase") or "Intermission"
	timerLabel.Text = formatTime(state:GetAttribute("TimeLeft"))
	if phase == "Round" then
		phaseLabel.Text = "ROUND"
	elseif phase == "Ended" then
		phaseLabel.Text = "ROUND OVER"
	else
		phaseLabel.Text = "INTERMISSION"
	end
	statusLabel.Text = state:GetAttribute("Status") or ""

	for index, def in ipairs(Config.Teams) do
		teamBoxes[index].Score.Text = tostring(state:GetAttribute("Score" .. index) or 0)

		local flagState = state:GetAttribute("Flag" .. index .. "State") or "Home"
		local carrier = state:GetAttribute("Flag" .. index .. "Carrier") or ""
		local text
		if flagState == "Carried" then
			text = "taken by " .. carrier
		elseif flagState == "Dropped" then
			text = "dropped on the field!"
		else
			text = "safe at base"
		end
		flagLabels[index].Text = def.Name .. " flag: " .. text
	end

	-- bottom alert
	local mine = myTeamIndex()
	local carrying = player:GetAttribute("CarryingFlag")
	if carrying then
		alertFrame.Visible = true
		alertFrame.BackgroundColor3 = Config.Teams[carrying].Colors[1]
		alertLabel.Text = "YOU HAVE THE FLAG! Run it back to your ring!"
	elseif mine and state:GetAttribute("Flag" .. mine .. "State") == "Carried" then
		alertFrame.Visible = true
		alertFrame.BackgroundColor3 = Color3.fromRGB(120, 20, 20)
		alertLabel.Text = "Your flag was stolen by " .. (state:GetAttribute("Flag" .. mine .. "Carrier") or "") .. "!"
	elseif mine and state:GetAttribute("Flag" .. mine .. "State") == "Dropped" then
		alertFrame.Visible = true
		alertFrame.BackgroundColor3 = Color3.fromRGB(120, 90, 20)
		alertLabel.Text = "Your flag is on the ground. Touch it to return it!"
	else
		alertFrame.Visible = false
	end
end

local announceToken = 0
announceRemote.OnClientEvent:Connect(function(text, color, duration, kind)
	announceToken += 1
	local token = announceToken
	announceLabel.Text = tostring(text)
	announceLabel.TextColor3 = (typeof(color) == "Color3") and color or WHITE
	announceLabel.TextTransparency = 0
	announceLabel.TextStrokeTransparency = 0.2
	playSound(kind)
	task.delay(tonumber(duration) or 3, function()
		if token ~= announceToken then
			return
		end
		TweenService:Create(announceLabel, TweenInfo.new(0.6), { TextTransparency = 1, TextStrokeTransparency = 1 }):Play()
	end)
end)

state.AttributeChanged:Connect(refresh)
player.AttributeChanged:Connect(refresh)
player:GetPropertyChangedSignal("Team"):Connect(refresh)
refresh()
