import pandas

# CSV ind Dataframe laden
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Dictionary aus Dataframe erzeugen
alphabeth_dict = { row.letter: row.code for (index, row) in data.iterrows()}

# Wort eingeben
word = input("Enter a word: ").upper()

# Liste mit Natoalphabet anhand des Wortes erzeugen
result = [alphabeth_dict[letter] for letter in word]
print(result)
