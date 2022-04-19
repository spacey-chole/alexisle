import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as coll

wid = 1
hei = 1
nrows = 7
ncols = 6
inbetween = 0.25

xx = np.arange(0, ncols, (wid+inbetween))
yy = np.arange(0, nrows, (hei+inbetween))
fig = plt.figure(figsize=(6, 7.25))

ax = plt.subplot(111, aspect = 'equal')
plt.xlim([-.25, 6.25])
plt.ylim([-0.25, 7.5])

pat = []
for xi in xx:
    for yi in yy:
        sq = patches.Rectangle((xi, yi), wid, hei, fill=True)
        ax.add_patch(sq)

pc = coll.PatchCollection(pat)
ax.add_collection(pc)

plt.title("alexisle")
plt.axis('off')
plt.show()
plt.savefig('test.png', dpi=90)