# PythonCityGgame

The "problem" we're solving is making a video game. Specifically, a two player competitive city builder game. City building is a fun genre, but it's typically for single player games. Multiplayer variants exist, but almost always revolve around each player having their own city, with the winner being the player with the best city.
We wanted a multiplayer city builder game that allowed for competition within one city. We wanted the core experience of building a city to be modified by the presence of another player, instead of following the traditional formula of one player per city.

## Requirements
 - Python 3.x
 - [Pygame](https://www.pygame.org): ```pip3 install pygame```
 
## Instructions
```python3 run.py```

Press ```h``` to see the help menu!

## Resources Used:
 - [Pygame Documentation](https://www.pygame.org/docs/)
 - [Pygame based game used for reference](https://github.com/Mekire/cabbages-and-kings)
 - [Pygame tutorials](https://nerdparadise.com/programming/pygame/part1)

## Main Features
 - Gameplay:
    * 2 player
    * Ability to easily add various levels (one comes with the game)
    * Each player can own buildings that generate profits based on the surrounding QoL
 - Game Board:
    * Each player can buy lots and build on them
    * Buildings can be demolished
    * 5 different building types
 - Mechanics:
    * Earn profits through buildings each round
    * Clickable grids and menus
    * Winning condition (reach 6000 dollars)
    * Dynamic turn order based on money

## Work division
 - John:
    * Game design and administration
    * QoL spreading
    * Several buildings, menus and their functionality
    * Several building assets
 - Homer:
    * Game design
    * Menus and owner info
    * Help menu
    * Various bug fixes
 - Christopher:
    * Game design
    * Turn structure
    * End game screen
    * Player classes
 - Tomas:
    * Base game window and project structure
    * Game mouse and keyboard event handling
    * Menu and Square templates
    * Level loading
    * Asset management and background music

---

## Asset Credits:
"Miami Viceroy" Kevin MacLeod (incompetech.com)\
Licensed under Creative Commons: By Attribution 3.0 License\
http://creativecommons.org/licenses/by/3.0/

"Cold Sober" Kevin MacLeod (incompetech.com)\
Licensed under Creative Commons: By Attribution 3.0 License\
http://creativecommons.org/licenses/by/3.0/
