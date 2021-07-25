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
- Ctrl-s to save map (in either mode)
- Ctrl-r to rotate current texture in hand (in either mode)

# Hacking 
- Resolution can be adjusted through the game/constants.py constants GAME_WIDTH, and GAME_HEIGHT
