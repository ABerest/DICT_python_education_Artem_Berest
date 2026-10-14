import random
print("HANGMAN!")
print('Guess the word!')
words = ['java', 'python', 'C++', 'javascript', 'php']
word = random.choice(words)
a = input("Guess the word:\n")

if a == word:
    print ('You Survived!')
else:
    print ('You lost!')
