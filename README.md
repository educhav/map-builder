# Simple Map Builder
- Simple platform-agnostic pixel-art map builder

## Quickstart
- Dependencies: pygame, numPy
```bash
pip install pygame numpy
git clone https://github.com/educhav/map-builder/
cd map-builder
python3 main.py "<mapfilename>.png"
```

# Controls
- ESCAPE: toggle menu mode (view textures)
- Ctrl-s: save map (in either mode)
- Ctrl-r: rotate current texture in hand 90 degrees (in either mode)
- Ctrl-l: load map passed in as second argument (python3 main.py "maptosave.png" "maptoload.png")
- LOAD does not work if you do not pass in a second argument as a map to load

# Hacking 
- Resolution can be adjusted through the game/constants.py constants GAME_WIDTH, and GAME_HEIGHT
