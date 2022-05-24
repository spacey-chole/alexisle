import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import keyboard as kbd


# width and height of squares
wid = 1
hei = 1

# number of rows and columns of squaresYes
nrows = 6
ncols = 5

# distance between squares?
inbetween = 0.25

# Create lists of x/y coordinates from 0 to the number of columns+1, with a step size of the square width
xx = np.arange(0, ncols + 1, (wid + inbetween))
yy = np.arange(0, nrows + 1, (hei + inbetween))

width = xx[4] + wid

# create figure for MatPlot
fig = plt.figure(figsize=(10, 10))

# create and set set limits for plot
ax = plt.subplot(111, aspect='equal')
plt.xlim([-.75, 6.75])
plt.ylim([- 3.25, 7.5])
# plt.axis('off')


#word guess grid

TOTAL_GUESSES = 6
LETTERS_PER_WORD = 5
status = []
letters = []

for i in range(TOTAL_GUESSES):
    statRow = []
    letterRow = []
    for j in range(LETTERS_PER_WORD):
        statRow.append("lightgrey")
        letterRow.append("")
    status.append(statRow)
    letters.append(letterRow)

#display word guess grid
guessSquares = []
dispLetters = []
for i in range(6):
    for j in range(5):
        xPos = xx[j]
        yPos = yy[5 - i]
        sq = patches.Rectangle((xPos, yPos), wid, hei, fill=True, color=status[i][j])
        guessSquares.append(sq)
        ax.add_patch(sq)

        #letters
        dispLetter = ax.text(xPos + wid / 2, yPos + hei / 2, letters[i][j], fontsize=30, horizontalalignment='center',
                        verticalalignment='center')
        dispLetters.append(dispLetter)



# qwerty keyboard
keyboard = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M"]]

# status of all the keys on the keyboard, appearently the authors were too lazy to write out "LightGrey" 26 times
keystat = []
for kbrow in (keyboard):
    for j in range(len(kbrow)):
        keystat.append("lightgrey")

# display keyboard
keywid = .5
keyhei = .8
keybetween = 0.05

kbSquares = []
kbDispLetters = []
for j in range(3):
    for i in range(len(keyboard[j])):

        xPos = ((keywid+keybetween)*i) + ((j+1)*keywid/2)
        if j == 2:
            xPos += keywid/2 + keybetween
        yPos = (keyhei+keybetween)*-j - keyhei - .3

        sq = patches.Rectangle((xPos, yPos), keywid, keyhei, fill=True, color="lightgrey")
        ax.add_patch(sq)
        kbSquares.append(sq)

        key = ax.text(xPos + keywid / 2, yPos + keyhei / 2, keyboard[j][i], fontsize=25, horizontalalignment='center',
                verticalalignment='center')
        kbDispLetters.append(key)


def update_board():
    numGuess = 0

    while numGuess < 6:
        word = []
        colors = []

        if kbd.is_pressed('space'):
            word = ["C", "R", "A", "N", "E"]
            colors = ["green", "green", "yellow", "green", "green"]
            numGuess += 1
            time.sleep(0.25)

        yield numGuess, word, colors


def animate(updates):
    guessNum, guessLetters, guessColors = updates
    guessNum -= 1

    if len(guessLetters) == 5:
        for i in range(5):
            guessSquares[5*guessNum+i].set_color(guessColors[i])
            dispLetters[5*guessNum+i].set_text(guessLetters[i])

            for j in range(len(keyboard)):
                for k in range(len(keyboard[j])):
                    if guessLetters[i] == keyboard[j][k]:
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

