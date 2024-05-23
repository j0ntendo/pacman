# Doboggi Man (Pac-Man)

Doboggi Man is a Pac-Man-like game written in Python. In this game, the player controls a character to eat Tteok-bokki while avoiding ghosts. The game utilizes the Turtle graphics library for visualization.

## Game Features

- Eat all the Tteok-bokki to advance to the next level.
- Avoid colliding with ghosts, as it will result in losing a life.
- The game ends when all the Tteok-bokki have been eaten or the player collides with a ghost.

## Installation

To run Doboggi Man, you need Python installed on your system. You can install Python from the official website: [python.org](https://www.python.org/)

After installing Python, clone or download the Doboggi Man repository to your local machine.

```bash
git clone <repository_url>
```

## Usage

Navigate to the `doboggi_man` directory in your terminal or command prompt, then run the `game.py` file using Python:

```bash
python game.py
```

Once the game starts, use the arrow keys to move Doboggi Man up, down, left, or right. Doboggi Man will automatically eat Tteok-bokki as it moves over them. Avoid colliding with ghosts, as it will result in losing a life.

Press the 'q' key to quit the game at any time.

## Files

- `game.py`: Main script containing the game logic and setup.
- `globals.py`: Contains global constants used in the game.
- `characters.py`: Defines the game characters such as ghosts and Doboggi Man.
- `p1.py`: Contains the `auto_doboggi_man` class for an autonomous Doboggi Man.
- `img/`: Directory containing images used in the game.


## License

This project is licensed under the Yonsei University guidelines for the Computer Programming class (CCO1100), covering teaching materials from 2016 to 2023. The materials provided are for personal use only and are not to be published or distributed publicly. This repository is intended solely for the purpose of my own portfolio and versioning. Any unauthorized distribution or publication of the course materials is prohibited. For private versioning, please use private repositories, as private GitHub repositories (git-based) are free of charge for university students.
