import random

def str2list(word):
    return [char for char in word]

def list2str(s):
    str1 = ""
    return(str1.join(s))

def ClearScreen():
    #print("\033[H\033[J", end="")    # Bildschirm löschen
    print("===== Welcome to hangman =====\n")
    

guess_words = []
MAX_GUESS = 6
num_guess = 0
wrong_guess = 0
solved_word = ""
guessed_char = ""

# more wordlists: http://www.gwicks.net/dictionaries.htm
inFile = open("wordlist_d.txt", "r", encoding='latin-1')
line = inFile.read()
guess_words = line.split()
chosen_word = guess_words[random.randint(0, len(guess_words)-1)]
solved_word_list = str2list("-" * len(chosen_word))
solved_word = list2str(solved_word_list)

print("===== Welcome to hangman =====\n")
print (f"{len(guess_words)} words loaded.\n")

while wrong_guess < MAX_GUESS and solved_word != chosen_word:
    print(solved_word)
    print(f"Wrong guesses: {wrong_guess}. Total guesses {num_guess}. Guessed chars: {guessed_char}")
    guess_char = input("Guess char: \n").lower()
    ClearScreen()
    if guess_char not in guessed_char:
        guessed_char += guess_char
        num_guess += 1
        char_pos = 0
        wrong_char = True
        for char in chosen_word:
            if guess_char == char:
                wrong_char = False
                solved_word_list[char_pos] = char
            char_pos += 1
            
        if wrong_char == True:
            wrong_guess += 1
        solved_word = list2str(solved_word_list)
    else:
        print("You've already had it!")
# --- Game over
if wrong_guess == 6:
    print (f"The word was {chosen_word}.")
else:
    print(f"You got it! - Wrong guesses: {wrong_guess}, Guesses needed {num_guess}.")


