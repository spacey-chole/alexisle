# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import random as rd
# from colorama import Fore, Back, Style, init
# import matplotlib.animation as animation
#
# # import gui
# #
# # gui.show()
#
# init(autoreset=True)
#
# # Joke word or not to joke word
# funTime = False
#
# # word list: awful, clumpy, butts, coagulant, poopy, cruel
# # whatever joke words my classmates have come up with
# funWords = ['awful', 'clumpy', 'butts', 'poopy',
#             'unfun', 'ducks', 'panda', "timmy", "TIMMY",
#             "jyang", "liang", "skyla", "adhoc", "antic",
#             'color', 'blind', 'chole', 'color', 'blind', 'chloe', 'cruel', 'vegan',
#             'idaho', "Lplus", "ratio", "chaos", "farts",
#             "amoeba", "among", "edwin", "dance", "david", "sussy",]
#
# # Reads csv file and assigns the column of potential words to an array of words
# wordsReal = pd.read_csv("Wordle.csv")
# wordsReal = wordsReal["validWordleAnswer"]
# # Gets rid of all the NaN values in the list
# wordsReal = wordsReal.dropna()
#
# # list of valid guesses
# validGuess = pd.read_csv("Wordle.csv")
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
# # correctWord = "paddy"
# guessWord = "_____"
#
# # sets counter for guesses
# numGuess = 0
#
#
# # to show board at the beginning
# #gui.update_board(1, 1, "yellow", "g")
# #gui.show()
#
#
# # while loop, iterates while the guess is wrong and numGuess is less than 5
# # No realli!
# while guessWord != correctWord and numGuess < 6:
#     # prints out your guess word so far
#     for char in guessWord:
#         print(char, end="")
#     print()
#
#     # sets guess-word to your input
#     guessWord = input()
#
#     # # check if word is valid guess
#     # while guessWord not in validGuess and guessWord not in wordsReal:
#     #     print("Not in word list")
#     #     guessWord = input()
#
#     correctLets = []
#     for j in correctWord:
#         correctLets.append(j)
#
#     # checks guess, and prints in terminal if the letter is in the right spot (green),
#     # if it is in the word but not in the right spot (yellow), or if the letter isn't in the word
#     # at the end, increment numGuess
#
#     # indices of guess word that are green/yellow
#     greenIn = []
#     yellowIn = []
#
#     for i in range(5):
#         if guessWord[i] == correctWord[i]:
#             correctLets.remove(guessWord[i])
#             greenIn.append(i)
#             print("added ", i, " to greenIns")
#
#     for i in range(5):
#         if correctLets.__contains__(guessWord[i]) and not greenIn.__contains__(guessWord[i]):
#             correctLets.remove(guessWord[i])
#             yellowIn.append(i)
#             print("added ", i, " to yellowIns")
#
#     print(greenIn)
#     print(yellowIn)
#
#     for i in range(5):
#         if greenIn.__contains__(i):
#             update_board(numGuess, i, "green", guessWord[i])
#             print(Back.GREEN + guessWord[i], end=" ")
#             plt.show()
#         elif yellowIn.__contains__(i):
#             update_board(numGuess, i, "khaki", guessWord[i])
#             print(Back.YELLOW + guessWord[i], end=" ")
#             plt.show()
#         else:
#             update_board(numGuess, i, "grey", guessWord[i])
#             print(guessWord[i], end=" ")
#             plt.show()
#
#     numGuess += 1
#     gui.show()
#
# # output messages depending on result
# if guessWord == correctWord:
#     print("You guessed the word")
# else:
#     print("The word was ", correctWord)
#
# fig = plt.figure(figsize=(10, 10))
# a = animation.FuncAnimation(fig, gui.animate, gui.update_board, blit=True, interval= 0.01)
# update_board(1, 1, "yellow", "g")
# plt.show()
#
# plt.title("alexisle")
#
#
# # import keyboard as kbd
#
# # https://stackoverflow.com/questions/44417945/creating-a-grid-of-squares-patches-in-matplotlib
#
# # width and height of squares?
# wid = 1
# hei = 1
#
# keywid = .5
# keyhei = .8
#
# # number of rows and columns of squaresYes
# nrows = 6
# ncols = 5
#
# # distance between squares?
# inbetween = 0.25
# keybetween = 0.05
#
# # Create lists of x/y coordinates from 0 to the number of columns+1, with a step size of the square width
# xx = np.arange(0, ncols + 1, (wid + inbetween))
# yy = np.arange(0, nrows + 1, (hei + inbetween))
#
# width = xx[4] + wid
#
# xkey = np.arange(0, 10, (keywid + inbetween))
# ykey = np.arange(-3, 0, (keyhei + inbetween))
#
# # create figure for MatPlot
# fig = plt.figure(figsize=(10, 10))
#
# # create and set setlimits for plot
# ax = plt.subplot(111, aspect='equal')
# plt.xlim([-.75, 6.75])
# plt.ylim([- 3.25, 7.5])
#
# # HI PRACCY
# # ax.text(3, 3, "hi", fontsize=20)
#
# # what is this for?
# pat = []
#
# # 2d array of the colors of each box, becuase the authors are too lazy to use OOP
# status = ["black", "black", "black", "black", "black",
#           "black", "black", "black", "black", "black",
#           "black", "black", "black", "black", "black",
#           "blue", "black", "black", "black", "black",
#           "black", "black", "black", "black", "black","black", "black", "black", "black", "black"]
# # 2d array of the guessed letters for each square
#
# letters = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
#
#
#
# # qwerty keyboard 2d array
# keyboard = [["Z", "X", "C", "V", "B", "N", "M"],
#             ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
#             ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]]
#
# # status of all the keys on the keyboard, appearently the authors were too lazy to write out "LightGrey" 26 times
# grey = "LightGrey"
# keystat = [["Black", "Black", "Black", "Black", "Black", "Black", "Black"],
#            ["Black", "Black", "Black", "Black", "Black", "Black", "Black", "Black", "Black"],
#            ["Black", "Black", "Black", "Black", "Black", "Black", "Black", "Black", "Black", "Black"]]
# for i in range(5):
#     for j in range(6):
#         # print(xx[i], yy[j])
#         sq = patches.Rectangle((xx[i], yy[5 - j]), wid, hei, fill=True, color=status[i+j*5])
#         ax.add_patch(sq)
# # for i in range(5):
# # for j in range(6):
# # ax.text(3, 3, letters,  fontsize=20)
#
# # display letters that user guessed
# for i in range(0, 5):
#     for j in range(0, 5):
#         ax.text(xx[i] + wid / 2, yy[5 - j] + hei / 2, letters[i+j*4], fontsize=30, horizontalalignment='center',
#                 verticalalignment='center')
#
# def update_board(row, position, color, letter):
#     # displaying colors
#     print("updating")
#     status[row][position] = color
#     letters[row][position] = letter
#     #for i in range(5):
#     #    for j in range(6):
#            # print(xx[i], yy[j])
#     #        sq = patches.Rectangle((xx[i], yy[5-j]), wid, hei, fill=True, color=status[j][i])
#     #        list.add(sq)
#     # for i in range(5):
#     # for j in range(6):
#     # ax.text(3, 3, letters,  fontsize=20)
#
#     # display letters that user guessed
#     for i in range(0, 4):
#         for j in range(0, 5):
#             ax.text(xx[i] + wid / 2, yy[5-j] + hei / 2, letters[j][i], fontsize=30, horizontalalignment='center',
#                     verticalalignment='center')
#
#     # display keyboard
#     for j in range(0, 3):
#         for i in range(len(keyboard[j])):
#             xkey = np.arange(0, width, len(keyboard[j])+keybetween)
#             sq = patches.Rectangle((xkey[i], ykey[j]), keywid, keyhei, fill=True, color=keystat[j][i])
#             ax.add_patch(sq)
#             ax.text(xkey[i] + keywid / 2, ykey[j] + keyhei / 2, keyboard[j][i], fontsize=30, horizontalalignment='center',
#                     verticalalignment='center')
#
#
#    # plt.show()
#     yield status, letters,
#
# plt.show()
#     # printing text on KEYBOARD
#     # for i in range(4):
#     # for j in range(len(keyboard[i])):
#     # ax.text(xkey[i], ykey[i], keyboard[i][j], color="yellow", fontsize = 10, horizontalalignment = 'center', verticalalignment='center')
#
#
# # pc = coll.PatchCollection(pat)
# # ax.add_collection(pc)
#
# def animate(changes):
#
#     # for i in range(0, 4):
#     #     for j in range(0, 5):
#     #         ax.text(xx[i] + wid / 2, yy[5-j] + hei / 2, letters[j][i], fontsize=30, horizontalalignment='center',
#     #                 verticalalignment='center')
#      for i in range(5):
#          for j in range(6):
#              sq = patches.Rectangle((xx[i], yy[5-j]), wid, hei, fill=True, color=status[j][i])
#              ax.add_patch(sq)
#     sta, le = changes
#     status = sta
#     letters = le
#
#     return status, letters,
#
# a = animation.FuncAnimation(fig, animate, update_board, blit=True, interval= 0.01)
#
# # we need to make the yield be something on the graph
# #def show():
#    # plt.show()
#
# # plt.axis('off')
#
# # plt.savefig('test.png', dpi=90)