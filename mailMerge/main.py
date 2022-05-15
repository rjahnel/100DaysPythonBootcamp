"""
TODO: Create a letter using starting_letter.docx
for each name in invited_names.txt
Replace the [name] placeholder with the actual name.
Save the letters in the folder "ReadyToSend".

Hint1: This method will help you:
https://www.w3schools.com/python/ref_file_readlines.asp
    Hint2: This method will also help you.
    https://www.w3schools.com/python/ref_string_replace.asp
        Hint3: This method will also help you.
        https://www.w3schools.com/python/ref_string_strip.asp
"""

PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    names = file.read()

name_list = names.split("\n")
print(name_list)

for name in name_list:
    with open("./Input/Letters/starting_letter.txt") as in_file:
        letter = in_file.read()
    file_name = f"./Output/ReadyToSend/letter_for_{name}.txt"
    with open(file_name, mode="w") as out_file:
        out_file.write(letter.replace(PLACE_HOLDER, name))
