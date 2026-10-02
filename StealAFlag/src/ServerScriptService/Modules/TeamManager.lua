--[[
	TeamManager
	Creates the two Team objects, puts joining players on the smaller team and
	rebalances at the start of every round.
]]

local Players = game:GetService("Players")
local Teams = game:GetService("Teams")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))

local TeamManager = {}
TeamManager.Teams = {}

local joinCounter = 0

function TeamManager.Init()
	for index, def in ipairs(Config.Teams) do
		local team = Teams:FindFirstChild(def.Name)
		if not team then
			team = Instance.new("Team")
			team.Name = def.Name
		end
		team.TeamColor = def.TeamColor
		team.AutoAssignable = false
		team.Parent = Teams
		TeamManager.Teams[index] = team
	end

	-- anything else in Teams would let players end up on a team the game does not know
	for _, team in ipairs(Teams:GetTeams()) do
		if not table.find(TeamManager.Teams, team) then
			team:Destroy()
		end
	end
end

function TeamManager.GetIndex(player)
	for index, team in ipairs(TeamManager.Teams) do
		if player.Team == team then
			return index
		end
	end
	return nil
end

function TeamManager.GetEnemyIndex(index)
	return (index == 1) and 2 or 1
end

function TeamManager.GetTeam(index)
	return TeamManager.Teams[index]
end

function TeamManager.Count(index)
	return #TeamManager.Teams[index]:GetPlayers()
end

function TeamManager.SetTeam(player, index)
	player.Team = TeamManager.Teams[index]
	player.Neutral = false
end

function TeamManager.AssignSmallest(player)
	joinCounter += 1
	player:SetAttribute("JoinOrder", joinCounter)

	local best, bestCount = 1, math.huge
	for index in ipairs(TeamManager.Teams) do
		local count = TeamManager.Count(index)
		if count < bestCount then
			best, bestCount = index, count
		end
	end
	TeamManager.SetTeam(player, best)
end

-- Moves the newest players off the bigger team until the sizes differ by at most one.
function TeamManager.Balance()
	for _, player in ipairs(Players:GetPlayers()) do
		if not TeamManager.GetIndex(player) then
			TeamManager.AssignSmallest(player)
		end
	end

	while true do
		local big, small = 1, 2
		if TeamManager.Count(2) > TeamManager.Count(1) then
			big, small = 2, 1
		end
		if TeamManager.Count(big) - TeamManager.Count(small) < 2 then
			break
		end

		local newest, newestOrder = nil, -1
		for _, player in ipairs(TeamManager.Teams[big]:GetPlayers()) do
			local order = player:GetAttribute("JoinOrder") or 0
			if order > newestOrder then
				newest, newestOrder = player, order
			end
		end
		if not newest then
			break
		end
		TeamManager.SetTeam(newest, small)
	end
end

return TeamManager
