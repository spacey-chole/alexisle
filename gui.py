import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as coll

# import keyboard as kbd

wid = 1
hei = 1
keywid = .2
keyhei = .1
nrows = 6
ncols = 5
inbetween = 0.25
xx = np.arange(0, ncols + 1, (wid + inbetween))
yy = np.arange(0, nrows + 1, (hei + inbetween))

xkey = np.arange(0, 10, (keywid + inbetween - .1))
ykey = np.arange(-3, 0, (keyhei + inbetween))

# create figure for MatPlot
fig = plt.figure(figsize=(10, 10))

ax = plt.subplot(111, aspect='equal')
plt.xlim([-10, 10])
# plt.keyxlim([])
plt.ylim([-10, 10])
ax.text(3, 3, "hi", fontsize=20)

pat = []
status = [[]]
keyboard = [[]]
letters = [[]]


def newgame():
    status = [["black", "black", "black", "black", "black"],
              ["black", "black", "black", "black", "black"],
              ["black", "black", "black", "black", "black"],
              ["black", "black", "black", "black", "black"],
              ["black", "black", "black", "black", "black"],
              ["black", "black", "black", "black", "black"]]
    letters = [["", "", "", "", ""],
               ["", "", "", "", ""],
               ["", "", "", "", ""],
               ["", "", "", "", ""],
               ["", "", "", "", ""],
               ["", "", "", "", ""]]
    keyboard = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
                ["Z", "X", "C", "V", "B", "N", "M"]]

def update_board(row, position, color, letter):
    # displaying colors
    for i in range(5):
        for j in range(6):
            print(xx[i], yy[j])
            sq = patches.Rectangle((xx[i], yy[j]), wid, hei, fill=True, color=status[i][j])
            ax.add_patch(sq)
    # for i in range(5):
    # for j in range(6):
    # ax.text( 3, 3, letters,  fontsize=20)

    # display keyboard
    num = len(keyboard[i])
    thing = ""
    for i in range(len(keyboard[i])):
        for v in range(num - 1):
            xkey = np.arange(0, num, (keywid + inbetween))

            thing += " "
        # for j in range(i*2-1):

        num -= 1;
        sq = patches.Rectangle((xkey[i], ykey[j]), keywid, keyhei, fill=True, color="black")

    print(thing)

# update_board(4, 1, "khaki", "G")
update_board(4, 2, "black", "Y")


def show():
    plt.show()


plt.title("alexisle")
# plt.axis('off')
plt.show()
plt.savefig('test.png', dpi=90)
