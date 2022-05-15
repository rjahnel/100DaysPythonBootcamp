import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R","S", "T", "U", "V",
           "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n","o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "$", "%", "#", "()", ")", "%", "#"]

print("=== Welcome to the pyPassword-Generator ====")
n_letters = int(input("How many letters: \n"))
n_numbers = int(input("How many numbers: \n"))
n_symbols = int(input("How many symbols: \n"))

l_password = []
for letter in range(1, n_letters + 1):
    l_password += random.choice(letters)

for number in range(1, n_numbers + 1):
     l_password += random.choice(numbers)

for symbol in range(1, n_symbols + 1):
     l_password += random.choice(symbols)

random.shuffle(l_password)

password = "".join(l_password)
print (f"Your new password is : {password}")

