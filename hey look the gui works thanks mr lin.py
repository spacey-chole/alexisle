import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import keyboard as kbd

import guesserfunctions

guesserfunctions.setup()

# create figure for MatPlot
fig = plt.figure(figsize=(10, 10))

# create and set limits for plot
ax = plt.subplot(111, aspect='equal')
plt.xlim([-.75, 6.75])
plt.ylim([- 3.25, 7.5])

# width and height of squares
guessW = 1
guessH = 1

# distance between squares?
inbetween = 0.25

# number of rows and columns of squaresYes
nrows = 6
ncols = 5

# Create lists of x/y coordinates from 0 to the number of columns+1, with a step size of the square width
guessXPos = np.arange(0, ncols + 1, (guessW + inbetween))
guessYPos = np.arange(0, nrows + 1, (guessH + inbetween))

keyboard = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M"]]

keyWidth = .5
keyHeight = .8
keyBtwn = 0.05

# to be updated and returned in animate()
guessSquares = []
dispLetters = []
kbSquares = []
kbDispLetters = []

# display guesses
for guessNum in range(6):
    for guessPos in range(5):
        xPos = guessXPos[guessPos]
        yPos = guessYPos[5 - guessNum]

        # boxes
        sq = patches.Rectangle((xPos, yPos), guessW, guessH, fill=True, color="lightgrey")
        guessSquares.append(sq)
        ax.add_patch(sq)

        # letters
        dispLetter = ax.text(xPos + guessW / 2, yPos + guessH / 2, "", fontsize=30, horizontalalignment='center',
                             verticalalignment='center')
        dispLetters.append(dispLetter)

# display keyboard
for kbRow in range(len(keyboard)):
    for rowPos in range(len(keyboard[kbRow])):

        centerOffset = ax.get_xlim()[0] + (ax.get_xlim()[1] - ax.get_xlim()[0] - (len(keyboard[0]) * (keyWidth + keyBtwn)))/2
        xPos = ((keyWidth + keyBtwn) * rowPos) + ((kbRow + 1) * (keyWidth+keyBtwn) * kbRow/4) + centerOffset
        yPos = (keyHeight + keyBtwn) * -(kbRow + keyHeight + .8)

        # boxes
        sq = patches.Rectangle((xPos, yPos), keyWidth, keyHeight, fill=True, color="lightgrey")
        ax.add_patch(sq)
        kbSquares.append(sq)

        # letters
        key = ax.text(xPos + keyWidth / 2, yPos + keyHeight / 2, keyboard[kbRow][rowPos], fontsize=25, horizontalalignment='center',
                      verticalalignment='center')
        kbDispLetters.append(key)


def update_board():
    numGuess = 0

    keepGoing = True

    while numGuess < 6:
        word = []
        colors = []

        if kbd.is_pressed('space') and keepGoing:

            word, colors = guesserfunctions.produce_guess()

            numGuess += 1
            time.sleep(0.25)

            keepGoing = False
            for c in colors:
                if c == "yellow" or c == "gray":
                    keepGoing = True

        yield numGuess, word, colors


def animate(updates):
    guessNum, guessLetters, guessColors = updates
    guessNum -= 1

    if len(guessLetters) == 5:
        for i in range(5):

            # set guess grid color and letters
            guessSquares[5*guessNum+i].set_color(guessColors[i])
            dispLetters[5*guessNum+i].set_text(guessLetters[i].upper())

            # find letter on keyboard and set color
            for j in range(len(keyboard)):
                for k in range(len(keyboard[j])):
                    if guessLetters[i].upper() == keyboard[j][k]:
                        if j == 0:
                            index = k
                        elif j == 1:
                            index = k + 10
                        else:
                            index = k + 19
                        kbSquares[index].set_color(guessColors[i])

    return *guessSquares, *dispLetters, *kbSquares, *kbDispLetters


a = animation.FuncAnimation(fig, animate, update_board, blit=True, interval=1)

plt.show()

