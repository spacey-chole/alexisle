import pandas as pd
import numpy as np

text_file = pd.read_csv()
wordArray = text_file.read().split(',')

actualWord = "which" #testing with this word
startingWord = "adieu"
currGuess = startingWord

correctLetters = ["","","","",""]

#this will be the for loop to check if the words finished
#while actualWord != "".join(correctLetters);

for l in range(len(currGuess)):
    if (l in actualWord):
        print(l)