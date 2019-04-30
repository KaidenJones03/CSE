import random
wordBank = ["Dog", "Cat", "Fish", "Turtle", "Lizard", "Hamster", "Chicken", "Pig", "Tiger", "Iguana", ]
Guesses = 8
word = random.choice(wordBank)
letters = []

print("Welcome to Hangman!")
print("Pick a letter")
# print(word)
list_of_letters_in_word = list(word)
hidden_word = list("*" * len(list_of_letters_in_word))
# print(hidden_word)

while Guesses > 0:
    print("".join(hidden_word))

    guess = input()
    letters.append(guess)
    print(letters)

    if guess in word:
        print("You got one")
        for i in range(len(word)):
            if list_of_letters_in_word[i] == guess:
                hidden_word[i] = list_of_letters_in_word[i]
    else:
        Guesses -= 1
        print("Wrong")
    print(Guesses)

    if Guesses <= 0:
        print("Game Over")

    elif hidden_word == list_of_letters_in_word:
        print("you win")
    print(hidden_word)
