--[[
	GameState
	Owns the ReplicatedStorage objects the client reads: a GameState folder whose
	attributes describe the match, and the Remotes folder. Everything is created
	on demand so the game also works when the scripts are pasted into Studio by hand.
]]

local ReplicatedStorage = game:GetService("ReplicatedStorage")

local GameState = {}

local function ensure(parent, name, className)
	local existing = parent:FindFirstChild(name)
	if existing then
		return existing
	end
	local instance = Instance.new(className)
	instance.Name = name
	instance.Parent = parent
	return instance
end

GameState.Folder = ensure(ReplicatedStorage, "GameState", "Folder")
GameState.Remotes = ensure(ReplicatedStorage, "Remotes", "Folder")

GameState.FireWeaponRemote = ensure(GameState.Remotes, "FireWeapon", "RemoteEvent")
GameState.WeaponFiredRemote = ensure(GameState.Remotes, "WeaponFired", "RemoteEvent")
GameState.AnnounceRemote = ensure(GameState.Remotes, "Announce", "RemoteEvent")

function GameState.Set(key, value)
	GameState.Folder:SetAttribute(key, value)
end

function GameState.Get(key)
	return GameState.Folder:GetAttribute(key)
end

-- Shows a message on every player's screen. `kind` picks the sound the client plays
-- ("info", "pickup", "drop", "return", "capture", "win").
function GameState.Broadcast(text, color, duration, kind)
	GameState.AnnounceRemote:FireAllClients(text, color or Color3.new(1, 1, 1), duration or 3, kind or "info")
end

-- Starting values so the HUD never reads nil.
GameState.Set("Phase", "Intermission")
GameState.Set("TimeLeft", 0)
GameState.Set("Status", "Starting up...")
GameState.Set("Score1", 0)
GameState.Set("Score2", 0)
GameState.Set("Flag1State", "Home")
GameState.Set("Flag2State", "Home")
GameState.Set("Flag1Carrier", "")
GameState.Set("Flag2Carrier", "")
GameState.Set("Winner", "")

return GameState
