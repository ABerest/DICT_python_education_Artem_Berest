import random

print("HANGMAN")
print()

words = ['java', 'python', 'javascript', 'php']
word = random.choice(words)
hidden = '-' * len(word)
guessedletter = []
attempts = 8

while attempts > 0:
    print(hidden)
    a = input("Input a letter: > ")

    if len(a) != 1:
        print("You should input a single letter")

    elif a not in 'abcdefghijklmnopqrstuvwxyz':
        print("Please enter a lowercase English letter")

    elif a in guessedletter:
        print("You've already guessed this letter")

    else:
        guessedletter.append(a)

        if a not in word:
            print("That letter doesn't appear in the word")
            attempts -= 1

        hiddenword = ''

        for letter in word:
            if letter in guessedletter:
                hiddenword += letter
            else:
                hiddenword += '-'

        hidden = hiddenword

        if hidden == word:
            print(f"You guessed the word {word}!")
            print("You survived!")
            break

else:
    print("You lost!")
