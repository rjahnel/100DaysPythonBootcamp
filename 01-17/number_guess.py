from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        return 0

def welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number beween 1 and 100.")

guess_number = randint(1, 100)
guessing = True
guesses = set_difficulty()

welcome()

while guessing:
    if guesses > 0:
        print (f"You have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess == guess_number:
            guessing = False
        elif guess < guess_number:
            print("Too low.\nGuess again.")
            guesses -= 1
        elif guess > guess_number:
            print("Too high.\nGuess again.")
            guesses -= 1
    else:
        guessing = False
        
if guesses == 0:
    print("You've run out of guesses, you lose.")   
elif guesses > 0:
    print(f"You got it! The answer was {guess}.") 
