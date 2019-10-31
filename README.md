# artillery

> A zero-, one-, or two-player artillery game with AI support.

## Setup

- Download the project with `git clone https://github.com/a11ce/artillery.git`.
- Run with `python3 artillery.py` or `./artillery.py`

## How to play

- Before starting, you may select the players (Human or various AIs) by entering their listed numbers one at a time.
- Each tank is represented by a colored box, purple for player 1 and blue for player 2.
- Human players enter a firing elevation angle (in degrees) and power (and AIs calculate their shots), then both shots are fired at the same time.
- The closer a shell lands to a tank, the more health it loses.
- The player whose tank loses all its health or falls out of the map first loses the game.

## File summary

- `artillery.py`: Game setup, main loop, and human move input.
- `fieldGen.py`: Map generation. 
- `graphics.py`: Console rendering of the map, tanks, and shells.
- `physics.py`: Projectile calculations for the shells.
- `impact.py`: Shell impacts including tank and terrain damage.
- `ai.py`: A few different AIs.
- `getch.py`: Cross-platform getch-like function. See URL at top of file.

--- 

All contributions are welcome by pull request or issue.

artillery is licensed under GNU General Public License v3.0. See [LICENSE](../master/LICENSE) for full text.