import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
import colorama as color

funTime = False

# word list: awful, clumpy, butts, coagulant, poopy, cruel

funWords = ['awful', 'clumpy', 'butts', 'coagulate', 'poopy',
            'unfun', 'ducks', 'panda', "timmy", "TIMMY",
            "jyang", "liang", "skyla", "adhoc", "antic",
            'color', 'blind', 'chole', 'color', 'blind', 'chloe', 'cruel', 'vegan',
            'idaho', "Lplus", "ratio", "chaos", "farts",
            "amoeba", "among", "edwin", "dance"]

wordsReal = pd.read_csv("Wordle.csv")
wordsReal = wordsReal["validWordleAnswer"]
wordsReal = wordsReal.dropna()
# print(wordsReal)

choiceIndex = rd.randint(0, len(wordsReal))
if (funTime):
    choiceIndex = rd.randint(0, len(funWords))
    choiceWords = funWords[choiceIndex]
else:
    choiceWord = wordsReal[choiceIndex]

print(choiceWord)

guessWord = "_____"

while (guessWord != choiceWord):
    for char in guessWord:
        print(char, end="")
    print()
    guessWord = input()
    for i in len(guessWord):
        if guessWord[i] == choiceWord[i]:
            print(color.Fore.GREEN + i, end="")
        elif (guessWord[i] in choiceWord):
            print(color.Fore.YELLOW + i, end="")
        else:
            print(i, end="")
        print()

