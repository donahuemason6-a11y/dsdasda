--[[
	Config
	Every tunable setting for Steal a Flag lives here. Both the server and the
	client require this module, so keep it free of server-only references.
]]

local Config = {}

Config.GameName = "Steal a Flag"

-- Team definitions. Team 1 owns the -X end of the arena, team 2 owns the +X end.
-- Colors[1] is the main colour (floor, player outline, HUD box). Every entry in
-- Colors is painted as a stripe on that team's flag and on the wall behind its base,
-- so a team can have two, three or more colours.
Config.Teams = {
	{
		Name = "Blue Team",
		TeamColor = BrickColor.new("Bright blue"),
		Colors = {
			Color3.fromRGB(13, 105, 172),
			Color3.fromRGB(128, 187, 219),
		},
	},
	{
		Name = "Red Team",
		TeamColor = BrickColor.new("Bright red"),
		Colors = {
			Color3.fromRGB(196, 40, 28),
			Color3.fromRGB(245, 205, 48),
		},
	},
}

-- Rounds
Config.CapturesToWin = 3
Config.RoundLength = 300 -- seconds
Config.IntermissionLength = 15 -- seconds between rounds
Config.RoundEndLength = 8 -- seconds the winner is shown
Config.MinPlayersToStart = 2 -- Studio play-testing always allows a single player

-- Flags
Config.PickupRadius = 5 -- studs from the flag needed to grab it
Config.CaptureRadius = 7 -- studs from your own flag stand needed to score
Config.FlagReturnTime = 20 -- seconds a dropped flag waits before going home by itself
Config.RequireOwnFlagHome = true -- classic rule: you cannot score while your own flag is away

-- Players
Config.RespawnTime = 4
Config.SpawnProtection = 3 -- seconds of forcefield after spawning
Config.WalkSpeed = 18
Config.FlagCarrierWalkSpeed = 15 -- carrying the flag slows you down a little

-- Weapon
Config.Weapon = {
	Name = "Blaster",
	Damage = 25,
	Cooldown = 0.3, -- seconds between shots
	Range = 250, -- studs
	FriendlyFire = false,
}

-- Map (all sizes in studs)
Config.Map = {
	Length = 280, -- X axis, base to base
	Width = 150, -- Z axis
	WallHeight = 26,
	BaseDepth = 60, -- how deep each team's coloured zone is
}

return Config
