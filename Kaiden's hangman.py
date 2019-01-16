import random
wordBank = ["Violin", "Banjo", "Guitar", "Ukulele", "Drums", "Piano", "Accordion", "Flute", "Clarinet", "Trumpet"]
Guesses = 8
word = random.choice(wordBank)
letters = []

print("Welcome to Hangman!")
print("Pick a letter")
print(word)

while Guesses > 0:
    guess = input()
    letters.append(guess)
    print(letters)
    Guesses -= 1
    if guess in word:
        print("You got one")
    else:
        Guesses -= 1
        print("Wrong")
    print(Guesses)

