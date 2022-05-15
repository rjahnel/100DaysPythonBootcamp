# -------------------------------
# Caesar encryption
# 
# from 100 days Python bootcamp
# --------------------------------

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n","o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n","o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message to encrypt: \n".lower())
shift = int(input("Type the shift number: \n"))

def caesar(plain_text, shift_amount, crypt_direction):
    
    cipher_text = ""
    shift_amount %= 25   # Verhindert einen Shift_amount > 24 (Array-Überlauf!)
    if crypt_direction == 'decode':
            shift_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text  += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text

print(f"Caesar {direction}d '{text}' to '{caesar(text, shift, direction)}'")