# AI Based Rock Paper Scissors Game

## Project Overview
This is a Python-based Rock Paper Scissors game that uses a simple AI approach to make predictions about the user’s next move. Instead of choosing randomly every time, the computer analyzes the user’s previous choices and tries to predict patterns.

The aim of this project is to demonstrate how basic artificial intelligence concepts such as pattern recognition and frequency analysis can be applied in a simple interactive game.

---

## How the Game Works
The game is played between the user and the computer.

- The user selects Rock, Paper, or Scissors.
- The computer records the user’s move history.
- It analyzes which moves are most frequently chosen.
- Based on this data, it predicts the next likely move.
- The computer then selects the move that can counter it.

This makes the computer slightly adaptive instead of purely random.

---

## AI Logic Used
The AI in this project is based on simple probability and frequency analysis:

- Stores all previous user moves
- Counts how often each move is used
- Predicts the most likely next move based on history
- Chooses the counter move to gain advantage

Although simple, this introduces the concept of predictive behavior in games.

---

## Features
- AI-based prediction system
- Score tracking for user and computer
- Draw detection
- Move history tracking
- Continuous gameplay in terminal

---

## How to Run the Project
1. Install Python 3.x if not already installed
2. Download or clone this repository
3. Open a terminal in the project folder
4. Run the program using:

```bash
python main.py
