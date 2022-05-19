import pandas as pd
import random

# text_file = open("words.txt", "r")
# A Møøse once bit my sister...
# wordArray = text_file.read().split('\n')

df = pd.read_csv("/Users/andrew/Desktop/python/Wordle/Wordle.csv")
df = df[df["validWordleAnswer"].notna()]
wordList = df["validWordleAnswer"].tolist()

frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

for q in range(1000):
    print(q)
    df = pd.read_csv("/Users/andrew/Desktop/python/Wordle/Wordle.csv")
    df = df[df["validWordleAnswer"].notna()]
    wordList = df["validWordleAnswer"].tolist()

    actualWord = wordList[random.randint(0,len(wordList))-1]
    # the word the computer guesses first
    startingWord = "crane"  # prounounced møøse and/or add - ee - ow
    secondWord = "shtik" # yolks
    thirdWord = "mould"
    # thirdWord = "" #tbd
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
    guessCount = 1
    # these for loop goes through the letters of the word, currguess is the current guess and actualword is the word
    # outer for loop goes through each letter in the computer's guess

    # TODO: remove letter from yellow list if we get it in the correct spot
    # TODO: also we need to account for if there's 2 of 1 letter
    # TODO: the guess gets stuck on yolks sometimes
    # TODO: track previous guesses so it doesnt guess the same thing again
    # while we haven't guessed the word yet and we haven't guessed too many times
    # (current is less than 20, but should probably be less than 6)
    # the "".join thing just turns the list of green letters into a word variable we can compare

    # everything in the code is within this while loop
    while "".join(greenLetters) != actualWord and guessCount != 7:
        # while loop to check if array of correct letters is the møøse
        # these for loop goes through the letters of the word, currguess is the current guess and actualword is the word
        # outer for loop goes through each letter in the computer's guess
        # print(currGuess, "has been added to the already guessed list")
        alreadyGuessed.append(currGuess)
        # for each letter in the current guess
        # print("check this guess: ", currGuess)
        # looking through each letter in the current guess, which starts as adieu
        for i in range(len(currGuess)):
            # just setting a new variable name currentletter to the current letter in the current guess
            currLetter = currGuess[i]
            for j in range(len(actualWord)):
                # for each letter in the word that is the solution
                wordLetter = actualWord[j]
                # check if letter in word, but in the wrong spot
                if currLetter == wordLetter and i != j:
                    # print(currLetter + " is in the word but not in the right place")
                    if currLetter not in greenLetters:
                        yellowLetters.append(currLetter)

                # the checker has found a letter that is in the same place both in the actualWord (the correct answer)
                # and in the computer's guess
                if currLetter == wordLetter and i == j:
                    # print(currLetter + " is in the word and in the right place")
                    greenLetters[i] = currLetter
                    # if currLetter in yellowLetters and letterTwice == False:
                    #     del yellowLetters[0]
            # if the currLetter belongs in lettersNotIn put it in there
            if (currLetter not in greenLetters) and (currLetter not in yellowLetters) and (currLetter not in lettersNotIn):
                lettersNotIn.append(currLetter)

        # make new guess
        # if no info about the word
        if len(yellowLetters) != 0 or greenLetters != ['_', '_', '_', '_', '_']:
            # iterates through word list backwards
            # starts at 2300 (the end)
            # w = len(wordList)-1
            # for w in reversed(range(len(wordList))):

            # TODO: things wrong in here
            # top of breakpoint
            #not working for some reason
            #TODO: trying another thing thursday where we do 2 for loops for each thing removing stuff
            # while w >= 0:
            # at end of while
            #     currWord = wordList[w]

            # hypothetically the nested whiles being coded above are going to ensure that currWord is set to a word at a valid index
            # # print("index of iteration?", w)  # surry
            # # print("length of reversed wordList: ", len(wordList))
            # if w > len(wordList) - 1:  # the length of your mom ;>
            #     print("too beeeeeg")
            #     print("the length:", len(wordList), "\nindex of iteration?", w)
            #     # NEW CHANGE MIGHT BREAK
            #     w = len(wordList)-1  # TODO: THIS IS A QUESTIONABLE FIX
            # if w < 0:
            #     print("too smoooooool")
            #     # NEW CHANGE MIGHT BREAK
            #     w = 0

            # count = 0
            if len(yellowLetters) != 0:
                for w in reversed(range(len(wordList))):
                    count = 0
                    # for each letter in the yellow letters list
                    for yl in yellowLetters:
                        # check if it is in the current word of the wordList
                        if yl in wordList[w]:
                            count += 1
                    # if the current word contains no yellow letters, delete from the list
                    if count == 0:
                        # print("deleting word using yellow:", wordList[w])
                        del wordList[w]
                        # w -= 1
                #goes through each letter in a word
            for w in reversed(range(len(wordList))):
                removed = False
                for i in range(len(wordList[w])):
                    #stuff wrong here somewhere
                    #this no work
                    if (wordList[w][i] != greenLetters[i] and greenLetters[i] != '_') or (wordList[w][i] in lettersNotIn):
                        # print("deleting word using green and not in:", wordList[w], wordList[w][i])
                        removed = True
                if (removed):
                    del wordList[w]

            # start scoring the remaining words
            if (guessCount > 2):
                highestScore = 0
                highestWord = ""
                for word in wordList:
                    if word not in alreadyGuessed:
                        word = word.lower()
                        wordScore = 0
                        for letter in range(len(word)):
                            wordScore += letterScores[word[letter]]
                            if word[letter] == greenLetters[letter]:
                                wordScore += 50
                        # print("score:", wordScore, "for word: ", word)
                        if wordScore > highestScore:
                            highestScore = wordScore
                            highestWord = word
                currGuess = highestWord
                # print("next guess:", currGuess)
                # print("word has a score:", highestScore)

                # make guess guess = møøse
            else:
                # this is if the first guess had no letters in the word
                if (guessCount == 1):
                    currGuess = secondWord
                else:
                    currGuess = thirdWord
            # else:
            #     currGuess = thirdWord
        # print(currGuess, "has been added to the alreadyGuessed list")
        alreadyGuessed.append(currGuess)
        # print(currGuess)
        # print(guessCount)
        guessCount += 1

    frequency[guessCount] += 1

    # print("green letters: ", greenLetters)  # swag letters
    # print("yellow letters: ", yellowLetters)  # slightly less swag letters
    # print("letters not in word ", lettersNotIn)  # not at all swag
    # print(wordList)
    # print("møøse")

print(frequency)
# Once upon a time, there was a møøse