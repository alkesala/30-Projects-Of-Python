class BmiCalc:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = self._normalize_height(height)
        self.bmi = None

    """Converts height from cm to m if it's greater than 2.5"""
    def _normalize_height(self, height):
        return height / 100 if height > 2.5 else height
    

    def calculate_bmi(self):
        """Calculates BMI"""
        try:
            self.bmi = self.weight / self.height ** 2
            return round(self.bmi, 2)
        except ZeroDivisionError:
            return "Invalid input"

    
    def get_bmi_category(self):
        """Get BMI category based on BMI value"""
        if self.bmi is None:
            self.calculate_bmi()
        
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal weight"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    @classmethod
    def get_user_input(cls):
        """Get user input for weight and height"""
        try:
            weight = float(input("Enter your weight: "))
            height = float(input("Enter your height: "))
            if weight <= 0 or height <= 0:
                raise ValueError("Height or weight cannot be less than or equal to 0")
            return cls(weight, height)
        except ValueError as e:
            print (f"Invalid input {e}")
            return None
        
    
    def __str__(self):
        """String representation of the object"""
        bmi = self.calculate_bmi()
        if isinstance(bmi, str):
            return "Error: Invalid measurements provided"
        return f"You're BMI is: {bmi} so you are: {self.get_bmi_category()}"
    
    

if __name__ == "__main__":
    bmi = BmiCalc(90, 180)
    print(bmi)

    print("\nEnter your measurements:")
    bmi1 = BmiCalc.get_user_input()
    if bmi1:
        print(bmi1)