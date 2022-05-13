import pandas as pd

# text_file = open("words.txt", "r")
# A Møøse once bit my sister...
# wordArray = text_file.read().split('\n')

df = pd.read_csv("/Users/andrew/Desktop/python/Wordle/Wordle.csv")
df = df[df["validWordleAnswer"].notna()]
wordList = df["validWordleAnswer"].tolist()
print("nan-, but not gluten-, -free wordList: ", wordList)

actualWord = "while"
# the word the computer guesses first
startingWord = "adieu"  # prounounced møøse
secondWord = "yolks"  # anticoagulant
# the computer's guesses
currGuess = startingWord

letterScores = {"e": 26, "a": 25, "r": 24, "i": 23, "o": 22, "t": 21, "n": 20, "s": 19, "l": 18, "c": 17,
                "u": 16, "d": 15, "p": 14, "m": 13, "h": 12, "g": 11, "b": 10, "f": 9, "y": 8, "w": 7,
                "k": 6, "v": 5, "x": 4, "z": 3, "j": 2, "q": 1}

# https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
# E	11.1607%56.88	M	3.0129%	15.36
# A	8.4966%	43.31	H	3.0034%	15.31
# R	7.5809%	38.64	G	2.4705%	12.59
# I	7.5448%	38.45	B	2.0720%	10.56
# O	7.1635%	36.51	F	1.8121%	9.24
# T	6.9509%	35.43	Y	1.7779%	9.06
# N	6.6544%	33.92	W	1.2899%	6.57
# S	5.7351%	29.23	K	1.1016%	5.61
# L	5.4893%	27.98	V	1.0074%	5.13
# C	4.5388%	23.13	X	0.2902%	1.48
# U	3.6308%	18.51	Z	0.2722%	1.39
# D	3.3844%	17.25	J	0.1965%	1.00
# P	3.1671%	16.14	Q	0.1962%	(1)


# these track the correct letters
# Mynd you, møøse bites Kan be pretti nasti...
# green
greenLetters = ['_', '_', '_', '_', '_']
# yellow
yellowLetters = []
# gray
lettersNotIn = []
# while loop to check if array of correct letters is the møøse
guessCount = 0
# these for loop goes through the letters of the word, currguess is the current guess and actualword is the word
# outer for loop goes through each letter in the computer's guess

def guess(currGuess):
    # while loop to check if array of correct letters is the møøse
    # these for loop goes through the letters of the word, currguess is the current guess and actualword is the word
    # outer for loop goes through each letter in the computer's guess
    for i in range(len(currGuess)):
        currLetter = currGuess[i]
        for j in range(len(actualWord)):
            wordLetter = actualWord[j]
            # check letterTwice
            letterTwice = False
            # check if letter in møøse, but in the wrong spot
            if currLetter == wordLetter and i != j:
                print(currLetter + " is in the word but not in the right place")
                yellowLetters.append(currLetter)
                letterTwice = True
            # the checker has found a møøse that is in the same place both in the actualWord (the correct answer)
            # and in the computer's guess
            if currLetter == wordLetter and i == j:
                print(currLetter + " is in the word and in the right place")
                greenLetters[i] = currLetter
                if currLetter in yellowLetters and letterTwice is False:
                    del yellowLetters[i]
        # if the currLetter belongs in lettersNotIn put it in there
        if (currLetter not in greenLetters) and (currLetter not in yellowLetters) and (currLetter not in lettersNotIn):
            lettersNotIn.append(currLetter)

    #get new guess
    #we're gonna need some sort of way to keep a score of a good guess

    # remove all words in wordArray that don't have the yellow/green letters
    # if yellow, remove all words with that letter in that slot
    # look through words.txt and see what the most common places for each letter is
    # so for example a appears most commonly in index 1 (idk if it does, just example)
    # so that's how you can prioritize møøse

    # try the list in a NEW PROGRAM to make it work because there are too many variables here

    # FIX THE REMOVE WORD THING YEAH
    if len(yellowLetters) != 0 and greenLetters != ['_', '_', '_', '_', '_']:
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
            # count checks if the word has any yellow letters (has a word that the right word also has)
            # if it does increment by 1
            # if the word has no yellow letters it removes it (no need to try and guess--it wont help us)
            # iterate through the yellowLetters list of words and check em all
            # yellow letters has to have letters to work
            if len(yellowLetters) != 0:
                for yl in yellowLetters:
                    # the loop has found a letter that is both in yellow letters and in the current word being guessed (currWord)
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
                            # pop removes the item at the specified index w from the list
                            # perhaps, aPOPtosis is the inspiration
                            # wordList.pop(w)
                            del wordList[w]
                            w -= 1

            # green letters has to have letters for this to run
            # this awful if statement is andrew's doing

            # for i in range(len(currWord)):
            #     # currWord[i] represents the current letter in the currWord being compared against the contents of our other lovely lists
            #     if (currWord[i] != greenLetters[i] and greenLetters[i] != '_') or (currWord[i] in lettersNotIn):
            #         print("deleting word using green and not in:", wordList[w])
            #             # pop removes the item at the specified index w from the list
            #             # perhaps, aPOPtosis is the inspiration
            #             # wordList.pop(w)
            #         del wordList[w]
            #         w -= 1

            # by now not swag words should be removed (hopefully)

        # this will generate the next guess based on how common the letters in a word are
        # in order to hopefully minimize the number of guesses the computer needs to get the word?

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
    return currGuess

def solve(guessCount, currGuess):
    allGuesses = []
    while "".join(greenLetters) != actualWord and guessCount != 5:
        currGuess = guess(currGuess)
        print("HAHAHAHAHAHSDFGSDHFAWYHDBFAJDHFBEAWHJBDFAS",currGuess)
        print(guessCount)
        guessCount += 1

solve(guessCount, currGuess)

print("green letters: ", greenLetters)  # swag letters
print("yellow letters: ", yellowLetters)  # slightly less swag letters
print("letters no in word ", lettersNotIn)  # not at all swag
print("møøse")
