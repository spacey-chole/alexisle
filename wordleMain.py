import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
from colorama import Fore, Back, Style, init
init(autoreset=True)

# Joke word or not to joke word
funTime = False

# word list: awful, clumpy, butts, coagulant, poopy, cruel
# whatever joke words my classmates have come up with
funWords = ['awful', 'clumpy', 'butts', 'coagulate', 'poopy',
            'unfun', 'ducks', 'panda', "timmy", "TIMMY",
            "jyang", "liang", "skyla", "adhoc", "antic",
            'color', 'blind', 'chole', 'color', 'blind', 'chloe', 'cruel', 'vegan',
            'idaho', "Lplus", "ratio", "chaos", "farts",
            "amoeba", "among", "edwin", "dance"]

# Reads csv file and assigns the column of potential words to an array of words
wordsReal = pd.read_csv("Wordle.csv")
wordsReal = wordsReal["validWordleAnswer"]
# Gets rid of all the NaN values in the list
wordsReal = wordsReal.dropna()

# list of valid guesses
validGuess = pd.read_csv("Wordle.csv")
validGuess = validGuess["validWordleGuess"].dropna()

# # selects a random index to use as the wordle word
# choiceIndex = rd.randint(0, len(wordsReal))
#
# # If joke words, assigns the guessing word from the joke word list
# # including the majestik møøse
# # if normal, assign to choiceIndex of choice words
# if funTime:
#     choiceIndex = rd.randint(0, len(funWords))
#     choiceWords = funWords[choiceIndex]
# else:
#     correctWord = wordsReal[choiceIndex]
# A Møøse once bit my sister...
correctWord = "mummy"
print(correctWord)

guessWord = "_____"

# sets counter for guesses
numGuess = 0

# while loop, iterates while the guess is wrong and numGuess is less than 5
# No realli!
while guessWord != correctWord and numGuess < 6:
    # prints out your guess word so far
    for char in guessWord:
        print(char, end="")
    print()

    # sets guess-word to your input
    guessWord = input()

    # # check if word is valid guess
    # while guessWord not in validGuess and guessWord not in wordsReal:
    #     print("Not in word list")
    #     guessWord = input()


    correctLets = []
    for j in correctWord:
        correctLets.append(j)

    # checks guess, and prints in terminal if the letter is in the right spot (green),
    # if it is in the word but not in the right spot (yellow), or if the letter isn't in the word
    # at the end, increment numGuess

    # indices of guess word that are green/yellow
    greenIn = []
    yellowIn = []

    for i in range(5):
        if guessWord[i] == correctWord[i]:
            correctLets.remove(guessWord[i])
            greenIn.append(i)
            print("added ", i, " to greenIns")

    for i in range(5):
        if correctLets.__contains__(i) and not greenIn.__contains__(guessWord[i]):
            correctLets.remove(guessWord[i])
            yellowIn.append(i)
            print("added ", i, " to yellowIns")

    print(greenIn)
    print(yellowIn)

    for i in range(5):
        if greenIn.__contains__(i):
            print(Back.GREEN + guessWord[i], end=" ")
        elif yellowIn.__contains__(i):
            print(Back.YELLOW + guessWord[i], end=" ")
        else:
            print(guessWord[i], end=" ")

    numGuess += 1

# output messages depending on result
if guessWord == correctWord:
    print("You guessed the word")
else:
    print("The word was ", correctWord)
