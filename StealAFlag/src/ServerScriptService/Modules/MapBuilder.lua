--[[
	MapBuilder
	Builds the whole arena from code when the server starts: floor, walls, cover,
	coloured base zones, flag stands and team spawns. Nothing has to be placed in
	Studio by hand. Returns a table describing each base so FlagManager can place the flags.
]]

local Workspace = game:GetService("Workspace")
local Lighting = game:GetService("Lighting")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Config = require(ReplicatedStorage:WaitForChild("Shared"):WaitForChild("Config"))

local MapBuilder = {}

local NEUTRAL_FLOOR = Color3.fromRGB(70, 72, 76)
local NEUTRAL_WALL = Color3.fromRGB(120, 122, 126)
local COVER_COLOR = Color3.fromRGB(99, 95, 98)

local function makePart(props)
	local part = Instance.new("Part")
	part.Anchored = true
	part.TopSurface = Enum.SurfaceType.Smooth
	part.BottomSurface = Enum.SurfaceType.Smooth
	local parent = props.Parent
	if props.CanCollide ~= nil then
		part.CanCollide = props.CanCollide -- must be set before CanQuery or CanTouch
	end
	for key, value in pairs(props) do
		if key ~= "Parent" and key ~= "CanCollide" then
			part[key] = value
		end
	end
	part.Parent = parent
	return part
end

local function folder(name, parent)
	local f = Instance.new("Folder")
	f.Name = name
	f.Parent = parent
	return f
end

-- Removes the Baseplate and spawn that a fresh Studio template ships with,
-- otherwise players could spawn in the middle of the arena.
local function clearTemplateObjects()
	for _, child in ipairs(Workspace:GetChildren()) do
		if child.Name == "Baseplate" or (child:IsA("SpawnLocation") and child.Name == "SpawnLocation") then
			child:Destroy()
		end
	end
end

local function buildFloorAndWalls(structure)
	local map = Config.Map
	local length, width, height = map.Length, map.Width, map.WallHeight

	makePart({
		Name = "Floor",
		Size = Vector3.new(length + 4, 4, width + 4),
		Position = Vector3.new(0, -2, 0),
		Color = NEUTRAL_FLOOR,
		Material = Enum.Material.Concrete,
		Parent = structure,
	})

	-- centre line
	makePart({
		Name = "CentreLine",
		Size = Vector3.new(1.5, 0.2, width),
		Position = Vector3.new(0, 0.1, 0),
		Color = Color3.fromRGB(235, 235, 235),
		Material = Enum.Material.SmoothPlastic,
		CanCollide = false,
		Parent = structure,
	})

	-- long side walls
	for _, sign in ipairs({ -1, 1 }) do
		makePart({
			Name = "SideWall",
			Size = Vector3.new(length + 4, height, 2),
			Position = Vector3.new(0, height / 2, sign * (width / 2 + 1)),
			Color = NEUTRAL_WALL,
			Material = Enum.Material.Brick,
			Parent = structure,
		})
	end

	-- end walls, painted in vertical stripes of the team that owns that end
	for teamIndex, def in ipairs(Config.Teams) do
		local sign = (teamIndex == 1) and -1 or 1
		local colors = def.Colors
		local stripeCount = #colors * 3
		local stripeWidth = (width + 4) / stripeCount
		for i = 1, stripeCount do
			local z = -(width + 4) / 2 + stripeWidth * (i - 0.5)
			makePart({
				Name = def.Name .. " Wall",
				Size = Vector3.new(2, height, stripeWidth),
				Position = Vector3.new(sign * (length / 2 + 1), height / 2, z),
				Color = colors[((i - 1) % #colors) + 1],
				Material = Enum.Material.SmoothPlastic,
				Parent = structure,
			})
		end
	end
end

local function buildCover(structure)
	-- One half of the arena (positive X). Every block is mirrored to the other side
	-- so both teams get exactly the same layout.
	local halfLayout = {
		{ pos = Vector3.new(28, 0, 12), size = Vector3.new(6, 7, 6) },
		{ pos = Vector3.new(28, 0, -12), size = Vector3.new(6, 7, 6) },
		{ pos = Vector3.new(55, 0, 0), size = Vector3.new(16, 5, 6) },
		{ pos = Vector3.new(55, 0, 40), size = Vector3.new(10, 6, 10) },
		{ pos = Vector3.new(55, 0, -40), size = Vector3.new(10, 6, 10) },
		{ pos = Vector3.new(80, 0, 22), size = Vector3.new(6, 9, 6) },
		{ pos = Vector3.new(80, 0, -22), size = Vector3.new(6, 9, 6) },
		{ pos = Vector3.new(35, 0, 58), size = Vector3.new(10, 12, 10) },
		{ pos = Vector3.new(35, 0, -58), size = Vector3.new(10, 12, 10) },
		{ pos = Vector3.new(105, 0, 50), size = Vector3.new(8, 4, 8) },
		{ pos = Vector3.new(105, 0, -50), size = Vector3.new(8, 4, 8) },
	}

	for _, entry in ipairs(halfLayout) do
		for _, sign in ipairs({ -1, 1 }) do
			local size = entry.size
			local pos = Vector3.new(entry.pos.X * sign, size.Y / 2, entry.pos.Z)
			makePart({
				Name = "Cover",
				Size = size,
				Position = pos,
				Color = COVER_COLOR,
				Material = Enum.Material.Slate,
				Parent = structure,
			})
		end
	end

	-- centre pillar blocks the straight shot from base to base
	makePart({
		Name = "CentrePillar",
		Size = Vector3.new(8, 16, 8),
		Position = Vector3.new(0, 8, 0),
		Color = COVER_COLOR,
		Material = Enum.Material.Slate,
		Parent = structure,
	})

	-- two low platforms you can hop on to
	for _, sign in ipairs({ -1, 1 }) do
		makePart({
			Name = "CentrePlatform",
			Size = Vector3.new(14, 3, 14),
			Position = Vector3.new(0, 1.5, sign * 28),
			Color = Color3.fromRGB(130, 130, 135),
			Material = Enum.Material.Concrete,
			Parent = structure,
		})
	end
end

local function buildBase(teamIndex, def, folders)
	local map = Config.Map
	local sign = (teamIndex == 1) and -1 or 1
	local mainColor = def.Colors[1]

	-- coloured floor zone
	local zoneCentreX = sign * (map.Length / 2 - map.BaseDepth / 2)
	makePart({
		Name = def.Name .. " Zone",
		Size = Vector3.new(map.BaseDepth, 0.2, map.Width),
		Position = Vector3.new(zoneCentreX, 0.1, 0),
		Color = mainColor,
		Material = Enum.Material.SmoothPlastic,
		Parent = folders.Bases,
	})

	-- flag stand: a short pedestal plus a glowing capture ring around it
	local standX = zoneCentreX
	local pedestal = makePart({
		Name = def.Name .. " Pedestal",
		Shape = Enum.PartType.Cylinder,
		Size = Vector3.new(0.6, 7, 7),
		CFrame = CFrame.new(standX, 0.3 + 0.2, 0) * CFrame.Angles(0, 0, math.rad(90)),
		Color = Color3.fromRGB(240, 240, 240),
		Material = Enum.Material.Marble,
		Parent = folders.Bases,
	})

	makePart({
		Name = def.Name .. " CaptureRing",
		Shape = Enum.PartType.Cylinder,
		Size = Vector3.new(0.15, Config.CaptureRadius * 2, Config.CaptureRadius * 2),
		CFrame = CFrame.new(standX, 0.28, 0) * CFrame.Angles(0, 0, math.rad(90)),
		Color = mainColor,
		Material = Enum.Material.Neon,
		Transparency = 0.45,
		CanCollide = false,
		CanQuery = false,
		CanTouch = false,
		Parent = folders.Zones,
	})

	-- spawns in a row behind the flag stand
	local spawnX = sign * (map.Length / 2 - 12)
	for i, z in ipairs({ -36, -12, 12, 36 }) do
		local spawn = Instance.new("SpawnLocation")
		spawn.Name = def.Name .. " Spawn " .. i
		spawn.Size = Vector3.new(6, 1, 6)
		spawn.Position = Vector3.new(spawnX, 0.5, z)
		spawn.Anchored = true
		spawn.TopSurface = Enum.SurfaceType.Smooth
		spawn.Color = mainColor
		spawn.Material = Enum.Material.SmoothPlastic
		spawn.TeamColor = def.TeamColor
		spawn.Neutral = false
		spawn.AllowTeamChangeOnTouch = false
		spawn.Duration = Config.SpawnProtection
		spawn.Parent = folders.Spawns
	end

	return {
		Index = teamIndex,
		Sign = sign,
		FlagStandPosition = Vector3.new(standX, pedestal.Position.Y + 0.3, 0),
	}
end

local function setupLighting()
	Lighting.ClockTime = 14
	Lighting.Brightness = 2
	Lighting.GlobalShadows = true
	Lighting.Ambient = Color3.fromRGB(90, 90, 95)
	Lighting.OutdoorAmbient = Color3.fromRGB(128, 128, 128)
	if not Lighting:FindFirstChildOfClass("Atmosphere") then
		local atmosphere = Instance.new("Atmosphere")
		atmosphere.Density = 0.25
		atmosphere.Parent = Lighting
	end
end

function MapBuilder.Build()
	clearTemplateObjects()

	local existing = Workspace:FindFirstChild("Map")
	if existing then
		existing:Destroy()
	end

	local mapFolder = folder("Map", Workspace)
	local folders = {
		Structure = folder("Structure", mapFolder),
		Bases = folder("Bases", mapFolder),
		Zones = folder("Zones", mapFolder),
		Spawns = folder("Spawns", mapFolder),
		Flags = folder("Flags", mapFolder),
	}

	buildFloorAndWalls(folders.Structure)
	buildCover(folders.Structure)

	local bases = {}
	for teamIndex, def in ipairs(Config.Teams) do
		bases[teamIndex] = buildBase(teamIndex, def, folders)
	end

	setupLighting()

	return {
		Folder = mapFolder,
		Folders = folders,
		Bases = bases,
	}
end

return MapBuilder
