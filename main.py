# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetics = {row["letter"]: row["code"] for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter the word: ").upper()
output = [nato_phonetics[letter] for letter in word]
print(output)
