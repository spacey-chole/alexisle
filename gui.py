import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as coll

wid = 1
hei = 1
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

ax = plt.subplot(111, aspect = 'equal')
plt.xlim([-.25,6.25])
plt.ylim([-0.25,7.5])

pat = []
for i in range(5):
    for j in range(6):
        print(xx[i], yy[j])
        sq = patches.Rectangle((xx[i], yy[j]), wid, hei, fill=True, color = status[i-1][j-1])
        ax.add_patch(sq)

pc = coll.PatchCollection(pat)
ax.add_collection(pc)

plt.title("alexisle")
plt.axis('off')
plt.show()
plt.savefig('test.png', dpi=90)