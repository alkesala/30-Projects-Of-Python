# BMI Calculator

**Description**  
This is a Python BMI (Body Mass Index) calculator class that calculates and categorizes a person's BMI based on their weight and height. The calculator supports both metric measurements and automatically converts height from centimeters to meters when needed. It provides detailed BMI categories and includes input validation for accurate results.

## Features

- **BMI Calculation**: Accurately calculates BMI using the formula weight/(height²)
- **Height Conversion**: Automatically handles height in both meters and centimeters
- **BMI Categories**: Classifies results into standard categories:
  - Underweight (< 18.5)
  - Normal weight (18.5 - 24.9)
  - Overweight (25 - 29.9)
  - Obese (≥ 30)
- **Input Validation**: Ensures valid weight and height measurements
- **User Input Support**: Provides an interactive way to enter measurements

## Usage

The calculator can be used in two ways:

```python
# Method 1: Direct instantiation
bmi = BmiCalc(90, 180)  # weight in kg, height in cm
print(bmi)

# Method 2: Interactive user input
bmi = BmiCalc.from_user_input()
if bmi:
    print(bmi)
```

## Input Requirements

- **Weight**: Positive number in kilograms (kg)
- **Height**: Positive number in either:
  - Meters (m): e.g., 1.80
  - Centimeters (cm): e.g., 180

## Error Handling

The calculator includes error handling for:

- Invalid input types
- Zero or negative measurements
- Missing input values

## Project Details

- **Author**: Aleksi
- **Date Created**: November 3, 2024
- **Difficulty Level**: Intermediate
