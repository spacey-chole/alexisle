import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as coll
import matplotlib.animation as animation
import keyboard as kbd


plt.title("alexisle")


# import keyboard as kbd

# https://stackoverflow.com/questions/44417945/creating-a-grid-of-squares-patches-in-matplotlib

# width and height of squares?
wid = 1
hei = 1

keywid = .5
keyhei = .8

# number of rows and columns of squaresYes
nrows = 6
ncols = 5
currentRow = 0

# distance between squares?
inbetween = 0.25
keybetween = 0.05

# Create lists of x/y coordinates from 0 to the number of columns+1, with a step size of the square width
xx = np.arange(0, ncols + 1, (wid + inbetween))
yy = np.arange(0, nrows + 1, (hei + inbetween))

width = xx[4] + wid

xkey = np.arange(0, 10, (keywid + inbetween))
ykey = np.arange(-3, 0, (keyhei + inbetween))

# create figure for MatPlot
fig = plt.figure(figsize=(10, 10))

# create and set setlimits for plot
ax = plt.subplot(111, aspect='equal')
plt.xlim([-.75, 6.75])
plt.ylim([- 3.25, 7.5])

# HI PRACCY
# ax.text(3, 3, "hi", fontsize=20)

# what is this for?
pat = []

# 2d array of the colors of each box, becuase the authors are too lazy to use OOP
status = ["black", "black", "black", "black", "black",
          "black", "black", "black", "black", "black",
          "black", "black", "black", "black", "black",
          "blue", "black", "black", "black", "black",
          "black", "black", "black", "black", "black","black", "black", "black", "black", "black"]
# 2d array of the guessed letters for each square

letters = [["", "", "", "", ""],
          ["", "", "", "", ""],
          ["", "", "", "", ""],
          ["", "", "", "", ""],
          ["", "", "", "", ""],
          ["", "", "", "", ""]]

# letters = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


if kbd.is_pressed('up'):
    print("test")
# qwerty keyboard 2d array
keyboard = [["Z", "X", "C", "V", "B", "N", "M"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]]

# status of all the keys on the keyboard, appearently the authors were too lazy to write out "LightGrey" 26 times
grey = "LightGrey"
keystat = [["Black", "Black", "Black", "Black", "Black", "Black", "Black"],
           ["Black", "Black", "Black", "Black", "Black", "Black", "Black", "Black", "Black"],
           ["Black", "Black", "Black", "Black", "Black", "Black", "Black", "Black", "Black", "Black"]]
for i in range(5):
    for j in range(6):
        # print(xx[i], yy[j])
        sq = patches.Rectangle((xx[i], yy[5 - j]), wid, hei, fill=True, color=status[j][i])
        ax.add_patch(sq)
# for i in range(5):
# for j in range(6):
# ax.text(3, 3, letters,  fontsize=20)

# display letters that user guessed
for i in range(0, 5):
    for j in range(0, 6):

        farts = ax.text(xx[i] + wid / 2, yy[5 - j] + hei / 2, letters[j][i], fontsize=30, horizontalalignment='center',
                verticalalignment='center')
print(status)
boxlist = []
textlist = []
def update_board(row, position, color, letter):
    while (True):
        # displaying colors
        print("updating")
        print(status)
        print(status[row][position])
        status[row][position] = color
        letters[row][position] = letter
        for i in range(5):
            for j in range(6):# print(xx[i], yy[j])
                sq = patches.Rectangle((xx[i], yy[5-j]), wid, hei, fill=True, color=status[j][i])
                boxlist.append(sq)

        # for i in range(5):
        # for j in range(6):
        # ax.text(3, 3, letters,  fontsize=20)
        currentRow = 0
        if kbd.is_pressed("return"):
        # display letters that user guessed
        #     for i in range(0, 4):
        #         for j in range(0, 5):
        #             farts = ax.text(xx[i] + wid/2, yy[5-j] + hei / 2, letters[j][i], fontsize=30, horizontalalignment='center',
        #                 verticalalignment='center')
        #             textlist.append(farts)


            print("test")
            # colorList = getColors();
            # nextWord = getGuess();
            #code to display word and color at current row

            currentRow = currentRow + 1
        yield textlist, boxlist,

    # display keyboard
    for j in range(0, 3):
        for i in range(len(keyboard[j])):
            xkey = np.arange(0, width, len(keyboard[j])+keybetween)
            sq = patches.Rectangle((xkey[i], ykey[j]), keywid, keyhei, fill=True, color=keystat[j][i])
            ax.add_patch(sq)
            ax.text(xkey[i] + keywid / 2, ykey[j] + keyhei / 2, keyboard[j][i], fontsize=30, horizontalalignment='center',
                    verticalalignment='center')


        # update_board(4, 1, "khaki", "G")
        # update_board(4, 2, "black", "Y")


   # plt.show()


 # printing text on KEYBOARD
    # for i in range(4):
    # for j in range(len(keyboard[i])):
    # ax.text(xkey[i], ykey[i], keyboard[i][j], color="yellow", fontsize = 10, horizontalalignment = 'center', verticalalignment='center')


# pc = coll.PatchCollection(pat)
# ax.add_collection(pc)
update_board(4,2,"yellow", "a")
plt.show()

# def animate(changes):
#     print("hello")
#     tl, bl = changes
#     # for i in range(0, 4):
#     #     for j in range(0, 5):
#     #         ax.text(xx[i] + wid / 2, yy[5-j] + hei / 2, letters[j][i], fontsize=30, horizontalalignment='center',
#     #                 verticalalignment='center')
#     # if (kbd.is_pressed("m")):
#     #     for i in range(5):
#     #         for j in range(6):
#     #             sq = patches.Rectangle((xx[i], yy[5-j]), wid, hei, fill=True, color=status[j][i])
#
#     return tl, bl,
#
# for i in range(len(textlist)):
#     ax.text(textlist[i])
# for i in range(len(boxlist)):
#     ax.add_patch(boxlist[i])
# a = animation.FuncAnimation(fig, animate, update_board, blit=True, interval= 0.01)
# # we need to make the yield be something on the graph
plt.show()


# plt.axis('off')

