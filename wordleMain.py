import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# word list: awful, clumpy, butts, coagulant, poopy, cruel

words = ['awful', 'clumpy', 'butts', 'coagulate', 'poopy',
         'unfun', 'ducks', 'panda', "timmy", "TIMMY",
         "jyang", "liang", "skyla", "adhoc", "antic",
         'color','blind', 'chole', 'chloe', 'cruel', 'vegan',
        'idaho', "Lplus", "ratio", "chaos", "farts",
         "amoeba", "among", "edwin"]

while True:
    randInt = np.random.randint(0, len(words))
    print(words[randInt])







plt.show()