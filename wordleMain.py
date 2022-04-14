import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd

# word list: awful, clumpy, butts, coagulant, poopy, cruel

words = ['awful', 'clumpy', 'butts', 'coagulate', 'poopy',
         'unfun', 'ducks', 'panda', "timmy", "TIMMY",
         "jyang", "liang", "skyla", "adhoc", "antic",
         'color','blind', 'chole', 'chloe', 'cruel', 'vegan',
        'idaho', "Lplus", "ratio", "chaos", "farts",
         "amoeba", "among", "edwin"]

wordsReal = pd.read_csv("Wordle.csv")
wordsReal = wordsReal["validWordleAnswer"]
wordsReal = wordsReal.dropna()
print(wordsReal)

choiceIndex = rd.randint(0, len(wordsReal))
choiceWord = wordsReal[choiceIndex]

print(choiceWord)
