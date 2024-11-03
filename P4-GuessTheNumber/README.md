# Number Guessing Game

**Description**  
A Python-based number guessing game where players try to guess a randomly generated number between 1 and 100. The game keeps track of attempts and total wins, and allows multiple rounds of play.

## Features

- **Random Number Generation**: Generates a random number between 1-100
- **Input Validation**: Ensures valid numeric input within the correct range
- **Feedback System**: Provides "Too high!" or "Too low!" hints
- **Score Tracking**: Keeps track of:
  - Total attempts
  - Total wins
- **Multiple Rounds**: Option to play multiple games
- **User-Friendly**: Clear prompts and error messages

## How to Play

```python
game = Game()
game.play()

# Example interaction:
# "Number generated!"
# "Enter your guess (1-100): " > 50
# "Too high!"
# "Enter your guess (1-100): " > 25
# "Too low!"
# "Enter your guess (1-100): " > 37
# "Correct!"
# "Want to play again?"
# "Enter 'yes' or 'no': "
```

## Game Rules

1. A random number between 1 and 100 is generated
2. Player enters their guess
3. Game provides feedback:
   - "Too high!" if guess is above target
   - "Too low!" if guess is below target
   - "Correct!" if guess matches
4. After winning, player can choose to:
   - Play again (new number generated)
   - End game (see final score)

## Methods

- `generate_number()`: Creates a new random number
- `get_guess()`: Gets and validates player input
- `check_guess()`: Compares guess with target number
- `play()`: Main game loop method

## Requirements

- Python 3.x
- random module (built-in)

## Project Details

- **Author**: Aleksi
- **Date Created**: November 3, 2024
- **Difficulty Level**: Beginner
- **Python Version**: 3.x
