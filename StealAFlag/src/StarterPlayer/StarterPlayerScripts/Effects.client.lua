--[[
	Effects
	Draws a tracer and impact flash for every shot the server reports.
	Everything here is local to this player's camera and never replicated.
]]

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Debris = game:GetService("Debris")
local Workspace = game:GetService("Workspace")
local TweenService = game:GetService("TweenService")

local remotes = ReplicatedStorage:WaitForChild("Remotes")
local weaponFired = remotes:WaitForChild("WeaponFired")

local SHOT_SOUND = "rbxasset://sounds/electronicpingshort.wav"

local function localPart()
	local part = Instance.new("Part")
	part.Anchored = true
	part.CanCollide = false
	part.CanQuery = false
	part.CanTouch = false
	part.CastShadow = false
	part.Material = Enum.Material.Neon
	return part
end

weaponFired.OnClientEvent:Connect(function(origin, endPosition, color)
	if typeof(origin) ~= "Vector3" or typeof(endPosition) ~= "Vector3" then
		return
	end
	local distance = (endPosition - origin).Magnitude
	if distance < 0.1 then
		return
	end
	color = (typeof(color) == "Color3") and color or Color3.new(1, 1, 1)
	local camera = Workspace.CurrentCamera

	local tracer = localPart()
	tracer.Name = "Tracer"
	tracer.Color = color
	tracer.Size = Vector3.new(0.12, 0.12, distance)
	tracer.CFrame = CFrame.lookAt(origin, endPosition) * CFrame.new(0, 0, -distance / 2)
	tracer.Parent = camera
	TweenService:Create(tracer, TweenInfo.new(0.12), { Transparency = 1 }):Play()
	Debris:AddItem(tracer, 0.15)

	local flash = localPart()
	flash.Name = "Impact"
	flash.Shape = Enum.PartType.Ball
	flash.Color = color
	flash.Size = Vector3.new(0.8, 0.8, 0.8)
	flash.Position = endPosition
	flash.Parent = camera
	TweenService:Create(flash, TweenInfo.new(0.2), { Size = Vector3.new(0.2, 0.2, 0.2), Transparency = 1 }):Play()
	Debris:AddItem(flash, 0.25)

	local sound = Instance.new("Sound")
	sound.SoundId = SHOT_SOUND
	sound.Volume = 0.4
	sound.PlaybackSpeed = 1.6
	sound.RollOffMaxDistance = 120
	local emitter = localPart()
	emitter.Transparency = 1
	emitter.Size = Vector3.new(0.1, 0.1, 0.1)
	emitter.Position = origin
	emitter.Parent = camera
	sound.Parent = emitter
	sound:Play()
	Debris:AddItem(emitter, 2)
end)
