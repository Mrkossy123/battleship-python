# Battleship Python Game

A simple Battleship game in Python for the university programming assignment.

## Description

This project implements a console-based Battleship game on a 5x5 board.  
The game supports:

- **1-player mode**: Player vs CPU
- **2-player mode**: Player vs Player

Each player has **5 ships**, and each ship occupies **one position** on the board.  
The objective is to sink all opponent ships before losing your own.

## Features

- 5x5 game board
- 5 ships per player
- Random ship placement for CPU
- Random first player selection
- Validation for ship positions
- Validation for missile positions
- Prevents duplicate ship placement
- Prevents duplicate missile throws
- Displays hits and misses after every turn

## How to Run

Make sure you have Python installed.

Run the game with:

```bash
py battleship.py
```

If your file is named differently, replace `battleship.py` with the correct filename.

## How to Play

1. Start the program
2. Choose:
   - `1` for 1-player game
   - `2` for 2-player game
3. Enter ship positions using coordinates like:
   - `a1`
   - `b3`
   - `e5`
4. During the game, enter missile positions using the same format

## Valid Positions

Rows:
- `a`
- `b`
- `c`
- `d`
- `e`

Columns:
- `1`
- `2`
- `3`
- `4`
- `5`

Example valid positions:
- `a1`
- `c4`
- `e5`

## Symbols on the Board

- `o` = hit
- `x` = miss

## File

- `battleship.py` : main game source code

## Notes

This project was created as part of a university assignment for an introductory programming course.

## Author
Konstantinos-Andrianos Kossyvakis
