--[[
	RoundManager
	The match loop: intermission -> round -> results, forever. A round ends when a
	team reaches Config.CapturesToWin or the clock runs out.
]]

local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))
local GameState = require(script.Parent:WaitForChild("GameState"))
local TeamManager = require(script.Parent:WaitForChild("TeamManager"))
local FlagManager = require(script.Parent:WaitForChild("FlagManager"))

local RoundManager = {}

local scores = { 0, 0 }
local roundOver = false

local function publishScores()
	GameState.Set("Score1", scores[1])
	GameState.Set("Score2", scores[2])
end

local function minPlayers()
	if RunService:IsStudio() then
		return 1
	end
	return Config.MinPlayersToStart
end

local function respawnEveryone()
	for _, player in ipairs(Players:GetPlayers()) do
		task.spawn(function()
			pcall(function()
				player:LoadCharacter()
			end)
		end)
	end
end

function RoundManager.AddCapture(teamIndex)
	scores[teamIndex] += 1
	publishScores()
	if scores[teamIndex] >= Config.CapturesToWin then
		roundOver = true
	end
end

local function runIntermission()
	GameState.Set("Phase", "Intermission")
	FlagManager.SetEnabled(false)
	FlagManager.ResetAll()

	local timeLeft = Config.IntermissionLength
	while timeLeft > 0 do
		local playerCount = #Players:GetPlayers()
		local needed = minPlayers()
		if playerCount < needed then
			GameState.Set("Status", string.format("Waiting for players (%d/%d)", playerCount, needed))
			GameState.Set("TimeLeft", Config.IntermissionLength)
			timeLeft = Config.IntermissionLength
		else
			GameState.Set("Status", "Next round starting soon")
			GameState.Set("TimeLeft", timeLeft)
			timeLeft -= 1
		end
		task.wait(1)
	end
end

local function runRound()
	scores = { 0, 0 }
	roundOver = false
	publishScores()
	GameState.Set("Winner", "")

	TeamManager.Balance()
	FlagManager.ResetAll()
	respawnEveryone()

	GameState.Set("Phase", "Round")
	GameState.Set("Status", string.format("First to %d captures wins", Config.CapturesToWin))
	GameState.Broadcast("Round started. Steal the enemy flag!", Color3.new(1, 1, 1), 4, "info")
	FlagManager.SetEnabled(true)

	local timeLeft = Config.RoundLength
	while timeLeft > 0 and not roundOver do
		GameState.Set("TimeLeft", timeLeft)
		task.wait(1)
		timeLeft -= 1
	end
	GameState.Set("TimeLeft", 0)
	FlagManager.SetEnabled(false)
end

local function showResults()
	GameState.Set("Phase", "Ended")

	local winnerIndex = nil
	if scores[1] > scores[2] then
		winnerIndex = 1
	elseif scores[2] > scores[1] then
		winnerIndex = 2
	end

	if winnerIndex then
		local def = Config.Teams[winnerIndex]
		GameState.Set("Winner", def.Name)
		GameState.Set("Status", def.Name .. " wins!")
		GameState.Broadcast(def.Name .. " wins the round!", def.Colors[1], Config.RoundEndLength, "win")
	else
		GameState.Set("Winner", "Draw")
		GameState.Set("Status", "It's a draw!")
		GameState.Broadcast("It's a draw!", Color3.new(1, 1, 1), Config.RoundEndLength, "win")
	end

	task.wait(Config.RoundEndLength)
end

function RoundManager.Start()
	FlagManager.OnCapture = RoundManager.AddCapture
	task.spawn(function()
		while true do
			runIntermission()
			runRound()
			showResults()
		end
	end)
end

return RoundManager
