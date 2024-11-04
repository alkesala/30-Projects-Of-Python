"""A random password generator for secure passwords."""

import random
import string

class PasswordGenerator:
    def __init__(self):
        self.password = ""
        self.generate_password()


    def generate_password(self):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
        self.password = random_string

        print(f"Your new password is: {self.password}")

if __name__ == "__main__":
    PasswordGenerator()
    
        