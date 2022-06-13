#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

guess_number = random.randint(1, 100)
remaining_guesses = 0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':
  remaining_guesses = 10
elif level == "hard":
  remaining_guesses = 5

game_on = True

while game_on and remaining_guesses > 0:
  print(f"You have {remaining_guesses} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == guess_number:
    print("You got it!")
    game_on = False
  elif guess < guess_number:
    print("Too low.")
  elif guess > guess_number:
    print("Too high.")
  remaining_guesses -= 1
  if remaining_guesses == 0:
    print("You run out of the guesses!")
  else:
    print("Guess again!")
    

