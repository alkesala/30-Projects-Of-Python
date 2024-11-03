import datetime

year_now = datetime.datetime.now().year
class GreetBot:

    def __init__(self):
        self.name = "GreetBot"
        self.greet = f"Hello, I am {self.name}, I am here to greet you."
        self.goodbye = "Goodbye, have a nice day"
        self.user_name = None
        self.user_age = None
        self.user_born_year = None


    def ask_user_name(self):
        self.user_name = input("What is your name? ")
        return f"Nice to meet you {self.user_name}!"
    
    def ask_user_age(self):
        self.user_age = input("How old are you? ")
        return f"Wow, you are {self.user_age} years old! So you were born in {self.calculate_user_born_year()}"

    def calculate_user_born_year(self):
        return year_now - int(self.user_age)
    
    def greet_user(self):
        print(self.greet)
        print(self.ask_user_name())
        print(self.ask_user_age())
        print(self.goodbye)

if __name__ == "__main__":
    bot = GreetBot()
    bot.greet_user()