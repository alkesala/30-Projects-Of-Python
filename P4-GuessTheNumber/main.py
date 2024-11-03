class Game:
    
    def __init__(self):
        self.number = None
        self.guess = None
        self.attempts = 0
        self.playing = True
        self.total_wins = 0

    def generate_number(self):
        from random import randint
        self.number = randint(1, 100)
        print("Number generated!")
        return self.number
    
    def get_guess(self):
        while True:
            try:
                self.guess = int(input("Enter your guess (1-100): "))
                if self.guess < 1 or self.guess > 100:
                    print("Guess must be a number between 1 and 100.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 100.")
        return self.guess
    
    
    def check_guess(self):
        if self.guess > self.number:
            print("Too high!")
        elif self.guess < self.number:
            print("Too low!")
        else:
            print("Correct!")
            self.total_wins += 1
            print("Want to play again?")
            play_again = input("Enter 'yes' or 'no': ")
            if play_again == "yes":
                self.attempts = 0
                self.generate_number()
            else:
                self.playing = False
            
        self.attempts += 1

    

    def play(self):
        self.generate_number()
        while self.playing:
            self.get_guess()
            self.check_guess()
        print(f"Total attempts: {self.attempts}. Total wins: {self.total_wins}.")

    


if __name__ == "__main__":
    game = Game()
    game.play()
