# Mario-Like Platformer Game

A fun 2D platformer game built with Python and Pygame, inspired by the classic Mario games!

## Features

✨ **Gameplay Features:**
- Player character with smooth movement and jumping mechanics
- Multiple levels (3 levels included) with increasing difficulty
- Enemies that patrol and can be defeated by jumping on them
- Collectible items to earn points
- Lives system - you start with 3 lives
- Score tracking throughout the game
- End flag to complete each level

## Installation

1. Make sure you have Python 3.7+ installed
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Clone or download this repository

## How to Play

```bash
python main.py
```

### Controls

| Key | Action |
|-----|--------|
| ← → | Move Left/Right |
| SPACE | Jump |
| R | Restart Current Level |
| N | Next Level (after game over or level complete) |

### Game Mechanics

- **Movement**: Use arrow keys to move left and right
- **Jumping**: Press space to jump. Jump on platforms to reach higher areas
- **Enemies**: Jump on enemies from above to defeat them and earn 100 points
- **Collectibles**: Collect gold coins to earn points (10-20 points each)
- **Lives**: You have 3 lives. Touching an enemy from the side loses a life. Falling off the screen also costs a life
- **Levels**: Reach the red flag at the end of each level to advance

## Game Structure

- `main.py` - Entry point for the game
- `game.py` - Main game loop and logic
- `player.py` - Player class with movement and physics
- `enemy.py` - Enemy class with AI patrol behavior
- `platform.py` - Platform class for level geometry
- `collectible.py` - Collectible items class
- `flag.py` - End level flag class
- `level.py` - Level management and creation
- `ui.py` - User interface and HUD

## Level Progression

### Level 1
Introductory level with basic platforms and a few enemies. Good for learning controls.

### Level 2
More challenging with narrow platforms and more enemies. Requires better timing and precision.

### Level 3
Final level with many enemies and tight platforming. Can you beat it?

## Customization

You can easily customize the game:

- **Add more levels**: Edit `level.py` and add `create_level_4()` methods
- **Change player speed**: Modify `Player.speed` in `player.py`
- **Adjust jump height**: Modify `Player.jump_power` in `player.py`
- **Change colors**: Edit the color tuples in each class (RGB format)
- **Modify difficulty**: Adjust enemy speed, platform placement, and collectible values

## Requirements

- Python 3.7+
- Pygame 2.0+

## License

Free to use and modify!

## Have Fun! 🎮

Enjoy the game and feel free to extend it with your own features!
