# Steal a Flag

A two-team capture-the-flag game for Roblox. Steal the other team's flag, carry it
back to the glowing ring at your base, and be the first team to three captures.

The whole arena is built by script when the server starts, so there is nothing to
place by hand in Studio.

## Opening it in Roblox Studio

**Fastest:** open `build/StealAFlag.rbxlx` in Roblox Studio and press Play.
That file is compiled from `src/` with [Rojo](https://rojo.space) and already
contains every script.

**With Rojo (for editing in VS Code):**

```
rojo build default.project.json -o build/StealAFlag.rbxlx
```

or `rojo serve` and connect from the Rojo Studio plugin.

**By hand (no tools):** create these objects in Studio and paste the matching file
into each one.

| Studio location | Object | Source file |
| --- | --- | --- |
| ReplicatedStorage > Shared (Folder) | ModuleScript `Config` | `src/ReplicatedStorage/Shared/Config.lua` |
| ServerScriptService | Script `Main` | `src/ServerScriptService/Main.server.lua` |
| ServerScriptService > Modules (Folder) | ModuleScript `GameState` | `src/ServerScriptService/Modules/GameState.lua` |
| ServerScriptService > Modules | ModuleScript `MapBuilder` | `src/ServerScriptService/Modules/MapBuilder.lua` |
| ServerScriptService > Modules | ModuleScript `TeamManager` | `src/ServerScriptService/Modules/TeamManager.lua` |
| ServerScriptService > Modules | ModuleScript `FlagManager` | `src/ServerScriptService/Modules/FlagManager.lua` |
| ServerScriptService > Modules | ModuleScript `CombatServer` | `src/ServerScriptService/Modules/CombatServer.lua` |
| ServerScriptService > Modules | ModuleScript `RoundManager` | `src/ServerScriptService/Modules/RoundManager.lua` |
| ServerStorage | Tool `Blaster` (set RequiresHandle on, CanBeDropped off) | |
| ServerStorage > Blaster | LocalScript `BlasterClient` | `src/ServerStorage/Blaster/BlasterClient.client.lua` |
| StarterPlayer > StarterPlayerScripts | LocalScript `HUD` | `src/StarterPlayer/StarterPlayerScripts/HUD.client.lua` |
| StarterPlayer > StarterPlayerScripts | LocalScript `Effects` | `src/StarterPlayer/StarterPlayerScripts/Effects.client.lua` |

The Blaster's handle, the remotes, the teams and the map are all created by the
scripts, so that table is the full setup.

## How to play

- You are put on the smaller team when you join. Blue Team spawns at one end of the
  arena, Red Team at the other.
- Click (or tap) with the Blaster equipped to shoot. Hold to keep firing.
  Four hits knock a player out; they respawn at their base a few seconds later.
- Walk into the enemy flag to steal it. Carrying it slows you down a little, and the
  whole server is told who has it.
- Bring the flag back to the glowing ring around your own flag stand to score.
  You cannot score while your own flag is away from its stand.
- If a carrier is knocked out the flag drops where they fell. Their team can touch it
  to return it, the enemy can pick it back up, and after twenty seconds it goes home
  on its own.
- First team to three captures wins the round. If the clock runs out first, the team
  with more captures wins.
- The leaderboard tracks Captures, Kills and Returns for every player.

## Changing things

Everything tunable is in `src/ReplicatedStorage/Shared/Config.lua`:

- Team names, team colours and the stripe colours painted on each flag and base wall.
- Captures needed to win, round length, intermission length, minimum players.
- Flag pickup and capture radius, auto-return time, whether your own flag must be home to score.
- Blaster damage, fire rate, range and friendly fire.
- Arena length, width, wall height and how deep each team's coloured zone is.

Cover placement lives in `MapBuilder.lua` (`buildCover`); every block listed there is
mirrored so both halves of the arena stay identical.

In Studio a round starts with a single player so you can test alone. On a live server
the game waits for `Config.MinPlayersToStart` players before starting a round.

## Layout

```
default.project.json              Rojo project
build/StealAFlag.rbxlx            compiled place file, open this in Studio
src/ReplicatedStorage/Shared/     Config (shared by server and client)
src/ServerScriptService/          Main script + Modules (map, teams, flags, combat, rounds)
src/ServerStorage/Blaster/        the weapon Tool and its client script
src/StarterPlayer/StarterPlayerScripts/   HUD and shot effects
```
