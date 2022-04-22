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
status = [["black","black","black","black","black"],
          ["black","black","black","black","black"],
          ["black","black","black","black","black"],
          ["black","black","black","black","black"],
          ["black","black","black","black","black"],
          ["black","black","black","black","black"]]

xx = np.arange(0, ncols + 1, (wid+inbetween))
yy = np.arange(0, nrows + 1, (hei+inbetween))
fig = plt.figure(figsize=(10,10))

def update_board():
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


pc = coll.PatchCollection(pat)
ax.add_collection(pc)

plt.title("alexisle")
# plt.axis('off')
plt.show()
plt.savefig('test.png', dpi=90)
