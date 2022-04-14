import pandas as pd

# text_file = open("words.txt", "r")
# wordArray = text_file.read().split('\n')

wordArray = pd.read_csv("Wordle.csv")
wordArray = wordArray["validWordleAnswer"]


print(wordArray)

#word is swagg
# goops
# g - [0]


actualWord = "which"
startingWord = "adieu"
backupWord = "golly"
currGuess = startingWord
closestGuess = "00000"

# guess apple
# word is among
# a - 0 1 2 3 4
# b - 0 1 2 3 4 (etc)
# so m would change to [0 2 3 4]
# p change to [0 3 4]
# l change to [0 1 2 4]

correctLetters = ['','','','','']
incorrectLetters = [[]]
lettersNotIn = []

# while actualWord != "".join(correctLetters):
for i in range(len(currGuess)):
    currLetter = currGuess[i]
    for j in range(len(actualWord)):
        wordLetter = actualWord[j]
        letterTwice = False
        if (currLetter == wordLetter and i != j):
            print(currLetter + " is in the word but not in the right place")
            #
            incorrectLetters.append(currLetter)
            incorrectLetters[currLetter].append(i)
            letterTwice = True
        if (currLetter == wordLetter and i == j):
            print(currLetter + " is in the word and in the right place")
            correctLetters[i] = currLetter
            if (currLetter in incorrectLetters and letterTwice == False):
                incorrectLetters.remove(currLetter)

    if (currLetter not in correctLetters) and (currLetter not in incorrectLetters):
        lettersNotIn.append(currLetter)
#get new guess
if  len(incorrectLetters) == 5:
    currGuess = backupWord
else:
    #generate new guess based on info
# for w in wordArray:
#     # finding words in the wordlist that match the stuff we've already found
#     # do we need to convert all the strings in wordArray into lists with 5 letters
#     # does w[i] work if w is a string
#     for i in range(len(correctLetters)):
#         if w[i] == correctLetters[i]:
#             print(w)
#             #word has letter in correct place
#         if w[i] in incorrectLetters:
#             print(w)
#             #word has letter but in wrong place

print(correctLetters)
print(incorrectLetters)
print(lettersNotIn)


