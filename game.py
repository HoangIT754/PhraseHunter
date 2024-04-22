from phrase import Phrase
import random


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("Moonlit forest"),
            Phrase("Haunted mansion"),
            Phrase("Stormy night"),
            Phrase("Empty hallway"),
            Phrase("Abandoned graveyard")
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("**********===========================**********")
        print("")
        print("            Welcome to Phrase Hunter           ")
        print("")
        print("**********===========================**********")

    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print("\nNumber missed: ", self.missed)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            self.active_phrase.display(self.guesses)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()
            
    def get_guess(self):
        user_guess = input("Enter your guess: ")
        return user_guess
    
    def game_over(self):
        if self.missed == 5:
            print("\nYou have missed 5 guesses. GAME OVER!")
        else:
            print("\nCongratulations! You WON!")

