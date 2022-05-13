import pandas as pd

# text_file = open("words.txt", "r")
# A Møøse once bit my sister...
# wordArray = text_file.read().split('\n')

df = pd.read_csv("/Users/andrew/Desktop/python/Wordle/Wordle.csv")
df = df[df["validWordleAnswer"].notna()]
wordList = df["validWordleAnswer"].tolist()
print("nan-, but not gluten-, -free wordList: ", wordList)

actualWord = "mercy"
# the word the computer guesses first
startingWord = "adieu"  # prounounced møøse
secondWord = "yolks"  # anticoagulant
# the computer's guesses
currGuess = startingWord

letterScores = {"e": 26, "a": 25, "r": 24, "i": 23, "o": 22, "t": 21, "n": 20, "s": 19, "l": 18, "c": 17,
                "u": 16, "d": 15, "p": 14, "m": 13, "h": 12, "g": 11, "b": 10, "f": 9, "y": 8, "w": 7,
                "k": 6, "v": 5, "x": 4, "z": 3, "j": 2, "q": 1}
greenLetters = ['_', '_', '_', '_', '_']
# yellow
yellowLetters = []
# gray
lettersNotIn = []
# words already guessed
alreadyGuessed = []

# while loop to check if array of correct letters is the møøse
guessCount = 0
# these for loop goes through the letters of the word, currguess is the current guess and actualword is the word
# outer for loop goes through each letter in the computer's guess

# TODO: remove letter from yellow list if we get it in the correct spot
# TODO: also we need to account for if there's 2 of 1 letter
# TODO: the guess gets stuck on yolks sometimes
# TODO: track previous guesses so it doesnt guess the same thing again
while "".join(greenLetters) != actualWord and guessCount != 20:
    # while loop to check if array of correct letters is the møøse
    # these for loop goes through the letters of the word, currguess is the current guess and actualword is the word
    # outer for loop goes through each letter in the computer's guess
    alreadyGuessed.append(currGuess)
    for i in range(len(currGuess)):
        currLetter = currGuess[i]
        for j in range(len(actualWord)):
            wordLetter = actualWord[j]
            # check letterTwice? does this work
            letterTwice = False
            # check if letter in møøse, but in the wrong spot
            if currLetter == wordLetter and i != j:
                print(currLetter + " is in the word but not in the right place")
                yellowLetters.append(currLetter)
                # letterTwice = True
            # the checker has found a møøse that is in the same place both in the actualWord (the correct answer)
            # and in the computer's guess
            if currLetter == wordLetter and i == j:
                print(currLetter + " is in the word and in the right place")
                greenLetters[i] = currLetter
                # if currLetter in yellowLetters and letterTwice == False:
                #     del yellowLetters[0]
        # if the currLetter belongs in lettersNotIn put it in there
        if (currLetter not in greenLetters) and (currLetter not in yellowLetters) and (currLetter not in lettersNotIn):
            lettersNotIn.append(currLetter)


# make new guess
    if len(yellowLetters) != 0 or greenLetters != ['_', '_', '_', '_', '_']:
        # iterates through word list backwards
        # starts at 2300
        for w in reversed(range(len(wordList))):
            # the iterating index? w seems to represent a number instead of a word which is wonky
            print("index of iteration?", w)  # surry
            print("length of reversed wordList: ", len(wordList))
            while w > len(wordList) - 1:  # the length of your mom ;>
                print("too beeeeeg")
                print("the length:", len(wordList), "\nindex of iteration?", w)
                w -= 1  # TODO: THIS IS A QUESTIONABLE FIX
            if w < 0:
                print("too smoooooool")
            currWord = wordList[w]

            count = 0
            if len(yellowLetters) != 0:
                for yl in yellowLetters:
                    if yl in currWord:
                        count += 1
                if count == 0:
                    print("deleting word using yellow:", wordList[w])
                    # wordList.pop(w)
                    del wordList[w]
                    w -= 1
                else:
                    for i in range(len(currWord)):
                        # currWord[i] represents the current letter in the currWord being compared against the contents of our other lovely lists
                        if (currWord[i] != greenLetters[i] and greenLetters[i] != '_') or (currWord[i] in lettersNotIn):
                            print("deleting word using green and not in:", wordList[w])
                            del wordList[w]
                            w -= 1
        highestScore = 0
        highestWord = ""
        for word in wordList:
            wordScore = 0
            for letter in word:
                wordScore += letterScores[letter]
            print("score:", wordScore, "for word: ", word)
            if wordScore > highestScore:
                highestScore = wordScore
                highestWord = word

        currGuess = highestWord
        print("next guess:", currGuess)
        print("word has a score:", highestScore)

        # make guess guess = møøse
    else:
        # this is if the first guess had no letters in the word
        currGuess = secondWord
    print(currGuess, " has been added to the alreadyGuessed list")
    alreadyGuessed.append(currGuess)
    print(currGuess)
    print(guessCount)
    guessCount += 1


print("green letters: ", greenLetters)  # swag letters
print("yellow letters: ", yellowLetters)  # slightly less swag letters
print("letters not in word ", lettersNotIn)  # not at all swag
# print("møøse")