import random
print("HANGMAN!")
print('Guess the word!')
words = ['java', 'python', 'javascript', 'php']
word = random.choice(words)
hidden = ('-' * len(word))
guessedletter = []
print (f'guess the word {hidden}')
attempts = 8
while attempts > 0:
    a = input ('your letter?\n')
    if a in word:
        guessedletter.append(a)
    else:
        print ('letter not guessed')
    attempts -= 1
    hiddenword = ''

    for letter in word:
        if letter in guessedletter:
            hiddenword += letter
        else:
            hiddenword += "-"

    if attempts > 0:
        print(hiddenword)

print("Thanks for playing!")
print("We'll see how well you did in the next stage")


