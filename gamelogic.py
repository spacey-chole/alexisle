import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
# from colorama import Fore, Back, Style, init

# import gui

# gui.show()

# init(autoreset=True)

# # Joke word or not to joke word
# funTime = False
#
# # word list: awful, clumpy, butts, coagulant, poopy, cruel
# # whatever joke words my classmates have come up with
# funWords = ['awful', 'clumpy', 'butts', 'coagulate', 'poopy',
#             'unfun', 'ducks', 'panda', "timmy", "TIMMY",
#             "jyang", "liang", "skyla", "adhoc", "antic",
#             'color', 'blind', 'chole', 'color', 'blind', 'chloe', 'cruel', 'vegan',
#             'idaho', "Lplus", "ratio", "chaos", "farts",
#             "amoeba", "among", "edwin", "dance", "david", "sussy"]
#
# # Reads csv file and assigns the column of potential words to an array of words
# wordsReal = pd.read_csv("Word Lists.csv")
# wordsReal = wordsReal["validWordleAnswer"]
# # Gets rid of all the NaN values in the list
# wordsReal = wordsReal.dropna()
#
# # list of valid guesses
# validGuess = pd.read_csv("Word Lists.csv")
# validGuess = validGuess["validWordleGuess"].dropna()
#
# # # selects a random index to use as the wordle word
# choiceIndex = rd.randint(0, len(wordsReal))
#
# # If joke words, assigns the guessing word from the joke word list
# # including the majestik møøse
# # if normal, assign to choiceIndex of choice words
# if funTime:
#     choiceIndex = rd.randint(0, len(funWords))
#     correctWord = funWords[choiceIndex]
# else:
#     correctWord = wordsReal[choiceIndex]
#
# # print("correct word:", correctWord)
# correctWord = "catch"
# guessWord = "_____"
#
# # sets counter for guesses
# numGuess = 0
#
#
# # to show board at the beginning
# #gui.update_board(1, 1, "yellow", "g")
# #gui.show()


def processGuess(guessWord, correctWord):
    # print(correctWord)
    #
    # for char in guessWord:
    #     print(char, end="")
    # print()

    # sets guess-word to your input
    # guessWord = input()

    # # check if word is valid guess
    # while guessWord not in validGuess and guessWord not in wordsReal:
    #     print("Not in word list")
    #     guessWord = input()

    correctLets = []
    for j in correctWord:
        correctLets.append(j)

    guessedLets = [let for let in guessWord]

    # checks guess, and prints in terminal if the letter is in the right spot (green),
    # if it is in the word but not in the right spot (yellow), or if the letter isn't in the word
    # at the end, increment numGuess

    # indices of guess word that are green/yellow
    greenIn = []
    yellowIn = []

    for i in range(5):
        if guessWord[i] == correctWord[i]:
            correctLets[i] = ""
            guessedLets[i] = ""
            greenIn.append(i)
            # print("added ", i, " to greenIns")

    for i in range(len(correctLets)):
        guessIndex = -1
        for j in range(len(guessedLets)):
            if guessedLets[j] != "" and correctLets[i] == guessedLets[j]:
                guessIndex = j
        if guessIndex > -1:
            guessedLets[guessIndex] = ""
            yellowIn.append(guessIndex)
            # print("added ", guessIndex, " to yellowIns")

    # print("green", greenIn)
    # print("yellow", yellowIn)

    colorList = []
    for i in range(5):
        if greenIn.__contains__(i):
            # gui.update_board(numGuess, i, "green", guessWord[i])
            # print(Back.GREEN + guessWord[i], end=" ")
            colorList.append("green")
            # gui.show()
        elif yellowIn.__contains__(i):
            # gui.update_board(numGuess, i, "khaki", guessWord[i])
            # print(Back.YELLOW + guessWord[i], end=" ")
            colorList.append("yellow")
            # gui.show()
        else:
            # gui.update_board(numGuess, i, "grey", guessWord[i])
            # print(guessWord[i], end=" ")
            colorList.append("gray")
            # gui.show()
    return colorList

# while loop, iterates while the guess is wrong and numGuess is less than 5
# No realli!
# while guessWord != correctWord and numGuess < 6:
#
#     guess = input("Enter your word: ")
#     colors = processGuess(guess, correctWord)
#     print()
#     print(colors)
#
#     numGuess += 1
#     # gui.show()
#
# # output messages depending on result
# if guessWord == correctWord:
#     print("You guessed the word")
# else:
#     print("The word was", correctWord)
