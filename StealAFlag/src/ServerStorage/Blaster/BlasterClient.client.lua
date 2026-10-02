--[[
	BlasterClient
	Runs inside the Blaster tool on each player's machine. It only reports where the
	player aimed; the server decides whether anything was hit.
]]

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")

local tool = script.Parent
local player = Players.LocalPlayer
local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))
local remotes = ReplicatedStorage:WaitForChild("Remotes")
local fireRemote = remotes:WaitForChild("FireWeapon")

local mouse = player:GetMouse()
local holding = false
local lastShot = 0

local function shoot()
	local now = os.clock()
	if now - lastShot < Config.Weapon.Cooldown then
		return
	end
	lastShot = now
	fireRemote:FireServer(mouse.Hit.Position)
end

-- Hold the button (or finger) down to keep firing.
tool.Activated:Connect(function()
	holding = true
	shoot()
	while holding and tool.Parent == player.Character do
		RunService.Heartbeat:Wait()
		shoot()
	end
end)

tool.Deactivated:Connect(function()
	holding = false
end)

tool.Unequipped:Connect(function()
	holding = false
end)
