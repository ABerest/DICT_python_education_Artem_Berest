import random

print("HANGMAN!")
print("Guess the word!")

words = ['java', 'python', 'javascript', 'php']
word = random.choice(words)
hidden = '-' * len(word)
guessedletter = []
attempts = 8

print(f'guess the word {hidden}')

while attempts > 0:
    a = input('your letter?\n')

    if a not in word:
        print("That letter doesn't appear in the word")
        attempts -= 1

    elif a in guessedletter:
        print("No improvements")
        attempts -= 1

    else:
        guessedletter.append(a)

    hiddenword = ''

    for letter in word:
        if letter in guessedletter:
            hiddenword += letter
        else:
            hiddenword += '-'

    if hiddenword == word:
        print("You guessed the word!")
        print("You survived!")
        break

    if attempts == 0:
        print("You lost!")
        break

    print(hiddenword)