# GreetBot

**Description**  
GreetBot is a simple Python interactive chatbot that greets users, collects their name and age, and calculates their birth year. The bot provides a friendly interface for basic user interaction and demonstrates object-oriented programming concepts in Python.

## Features

- **User Interaction**: Collects user's name and age through interactive prompts
- **Birth Year Calculation**: Automatically calculates user's birth year based on current year
- **Friendly Responses**: Provides personalized greetings and responses
- **Current Year Detection**: Uses system date to ensure accurate birth year calculations

## Usage

```python
# Create and run the bot
bot = GreetBot()
bot.greet_user()

# Example interaction:
# "Hello, I am GreetBot, I am here to greet you."
# "What is your name? "
# > John
# "Nice to meet you John!"
# "How old are you? "
# > 25
# "Wow, you are 25 years old! So you were born in 1999"
# "Goodbye, have a nice day"
```

## Methods

- `ask_user_name()`: Prompts for and stores user's name
- `ask_user_age()`: Prompts for and stores user's age
- `calculate_user_born_year()`: Calculates birth year based on age
- `greet_user()`: Main method that handles the complete interaction flow

## Requirements

- Python 3.x
- datetime module (built-in)

## Project Details

- **Author**: Aleksi
- **Date Created**: November 3, 2024
- **Difficulty Level**: Beginner
- **Python Version**: 3.x
