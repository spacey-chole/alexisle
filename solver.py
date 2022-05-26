import pandas as pd
import random
from PIL import Image

df = pd.read_csv("Word Lists.csv")
df = df[df["validWordleAnswer"].notna()]
word_list = df["validWordleAnswer"].tolist()
# print("wordList: ", word_list)

# actual_word = str(random.choices(word_list))
# # have to remove the [' '] from the actual word. i hate the .choices method
# actual_word = actual_word[2: 7]
actual_word = "house"
print("actual_word: ", actual_word)

starting_word = "crane"

green_letters = ["_", "_", "_", "_", "_"]
yellow_letters = []
gray_letters = []
guess_count = 0

# these lists seem poorly named, but they make sense
# these were created because deleting things out of lists
    # (i tried remove(), pop(), and del() just messed up the indexes)

# ok_words represents the list of words that make sense for the computer to guess
# after the words containing gray letters are filtered out from the word list
# (so, in an ideal world, it would the word_list with gray-letter-containing-words removed)
ok_words = []
# ok_words_2 represents the list of words that make sense for the computer to guess
# after the words with green letters not in the right are filtered out from the word list
# (so, in an ideal world, it would the word_list with green-letter-not-in-the-right-place-words removed)
ok_words_2 = []
# ok_words_3 represents the list of ok_words_2 with curr_guess removed.
# might be unnecessary but don't want to change in case it breaks
ok_words_3 = []

words_remaining = [w for w in word_list if w != starting_word]

# TODO: edit the get_next_guess() method to pick a smarter guess so it gets it every time
#   first pick highest scoring, then from there pick most different
#   (just reverse the order in which the smarter_guesses thing is made)
#   or pick a different starting word than "crane," do the weird analysis thing

# picking the "fittest" guess to most greatly increase our chances of getting the solution word (actual_word)
# things to consider when picking the next guess:
     # the highest scoring word
     # a word with completely different letters than the first guess to see the status of more potential letters
     # only pulling from the available pool

# what the method currently does:
    # using the already filtered list from gray and green letters (smart_guesses),
    # find the word with the most difference of letters from the original word (max = 5--all diff, min = 0--all same)
    # this uses the "highest_diff" var
    # put all the words with the maximum number of different letters into their own list because deleting no worky
    # then of the diverse words in the new list (smarter_guesses) go pick the word with the highest score,
    # based on letter frequency [and also green and yellow contents checks -- might be wrong]


def get_next_guess(smart_guesses, prev_guess):
    # pick words that have the most letters than the first guess
    # highest_diff represents the maximum number of letters different from the original list are in the smart guesses
    highest_diff = 0
    diff = 0
    # finding highest_diff
    for i in range(len(smart_guesses)):
        poss_guess = smart_guesses[i]
        # print("poss_guess:", poss_guess)
        for j in range(len(poss_guess)):
            # print(" is", poss_guess[j], "in", prev_guess, "?")
            if poss_guess[j] not in prev_guess:
                # print(" no it isn't")
                diff += 1
                # print("poss_guess: ", poss_guess, "diff:", diff)
            # else:
            #  print(" yes it is, do nothing")
        if diff > highest_diff:
            highest_diff = diff
            # print(" highest_diff: ", diff)
        diff = 0

    # now that we know the most possible letters we can differ, put the highest_diff words into a new list
    smarter_guesses = []
    for word in smart_guesses:
        poss_guess = word
        # print("poss_guess:", poss_guess)
        for letter in poss_guess:
            # print(" is", prev_guess[j], "in", poss_guess, "?")
            if letter not in prev_guess:
                # print(" no it isn't")
                diff += 1
                # print(" poss_guess:", poss_guess, "diff:", diff)
            # else:
            # print(" yes it is, do nothing")
        if diff == highest_diff:
            smarter_guesses.append(poss_guess)
        diff = 0
    # print("smarter guesses: ", smarter_guesses)
    # then, use the highest score based on letter frequency thing to pick the smartest of the smarter_guesses
    # now that we know the most possible letters we can differ, put the highest_diff words into a new list

    # Original: letterScores = {"e": 26, "a": 25, "r": 24, "i": 23, "o": 22, "t": 21, "n": 20, "s": 19, "l": 18, "c": 17,
    #                 "u": 16, "d": 15, "p": 14, "m": 13, "h": 12, "g": 11, "b": 10, "f": 9, "y": 8, "w": 7,
    #                 "k": 6, "v": 5, "x": 4, "z": 3, "j": 2, "q": 1}

    # rounded by 5 letter scores
    letterScores = {"e": 30, "a": 30, "r": 30, "i": 30, "o": 30, "t": 25, "n": 25, "s": 25, "l": 25, "c": 25,
                    "u": 20, "d": 20, "p": 20, "m": 20, "h": 20, "g": 15, "b": 15, "f": 15, "y": 15, "w": 15,
                    "k": 10, "v": 10, "x": 10, "z": 10, "j": 10, "q": 10}

    highest_score = 0
    highest_word = ""
    if len(smarter_guesses) == 1:
        new_guess = smarter_guesses[0]
    for word in smarter_guesses:
        score = 0
        word = word.lower()
        for letter in range(len(word)):
            # frequency
            score += letterScores[word[letter]]
            # based on green_letters
            # if word[letter] == green_letters[letter]:
            #    score += 50
            # based on yellow_letters
            for letterY in yellow_letters:
                if letterY in word:
                    score += 50
        if score > highest_score:
            highest_score = score
            highest_word = word
        # print("word: ", word, ", score:", score)
    # print("     highest_score:", highest_word)
    return highest_word

while guess_count < 6:
    print()
    if guess_count == 0:
        curr_guess = starting_word
    # wiping the two ok_words lists
    # since gray, green, and yellow letter lists update continuously, the next ok_words lists will be re-updated properly
    ok_words = []
    ok_words_2 = []
    ok_words_3 = []
    # the highlight is saying that 'curr_guess' can be undefined.
    # that would only happen if we don't give starting_word a value above, so don't do that
    print("curr_guess: ", curr_guess)
    print("guess_count: ", guess_count)
    # sorting the letters in the guess word into the proper lists/categories based on the actual word
    print("sorting letters into the lists...")
    for i in range(len(curr_guess)):
        guess_letter = curr_guess[i]
        for j in range(len(actual_word)):
            actual_letter = actual_word[j: j+1]
            # there is a letter in both the actual_word and the curr_guess (a letter is correct)
            # print(guess_letter, " in the guess is being compared to ", actual_letter)
            if guess_letter == actual_letter:
                # now, check if it is yellow or green
                if i == j:
                    # same location and same letter
                    # print(" adding", guess_letter, "to green letters")
                    green_letters[i] = guess_letter
                elif i != j:
                    # trying to avoid adding duplicates to yellow_letters
                    if guess_letter not in yellow_letters:
                        # print(" adding", guess_letter, "to yellow letters")
                        yellow_letters.append(guess_letter)
    print("green_letters: ", green_letters)
    # TODO: clean out yellow_letters once more guesses are made because once we find where a letter goes
    #  (put it in green_letters) we no longer need to keep it in yellow_letters
    #   this seems to be messing up the scoring of the words in the letter checker

    print("yellow_letters: ", yellow_letters)
    for i in range(len(curr_guess)):
        guess_letter = curr_guess[i]
        if (guess_letter not in green_letters) and (guess_letter not in yellow_letters) and (guess_letter not in gray_letters):
            # print(" adding", guess_letter, "to gray letters")
            gray_letters.append(curr_guess[i])
    print("gray_letters: ", gray_letters)

    # now filtering the word list by deleting things that shouldn't be guessed because we know they're wrong
    # start by deleting based on gray letters
    print("filtering by gray letters...")
    for word in range(len(words_remaining)):
        curr_word = words_remaining[word]
        ok = True
        for letter in range(len(gray_letters)):
            if gray_letters[letter] in curr_word:
                ok = False
        if ok:
            ok_words.append(curr_word)
    if 'FALSE' in ok_words:
        ok_words.remove('FALSE')
    print("ok_words: ", ok_words)
    # questionable fix, but it did work
    # for some reason, FALSE (yes in all caps) would occasionally get added to the list of ok_words
    # (which is not ok)
    # so I had to remove it by hand, because the solver would get stuck on it and keep guessing "FALSE"
    # I thought it was something wrong with not removing the curr_guess, but that was not the problem
    # also see below
    print("filtering by green letters...")
    for word in range(len(ok_words)):
        curr_word = ok_words[word]
        ok = True
        for letter in range(len(green_letters)):
            # print("curr_word", curr_word, "being checked for", green_letters[letter])
            if (curr_word[letter] != green_letters[letter]) and (green_letters[letter] != "_"):
                # print(curr_word, "doesn't have", green_letters[letter], "in the right spot. not ok.")
                ok = False
        if ok:
            ok_words_2.append(curr_word)
        # questionable fix, but it did work
        # for some reason, FALSE (yes in all caps) would occasionally get added to the list of ok_words
        # (which is not ok)
        # so I had to remove it by hand, because the solver would get stuck on it and keep guessing "FALSE"
        # I thought it was something wrong with not removing the curr_guess, but that was not the problem
        # also see above
        if 'FALSE' in ok_words_2:
            ok_words.remove('FALSE')
    print("ok_words_2:", ok_words_2)
    # picking next guess and incrementing guess_count
    guess_count += 1

    for word in ok_words_2:
        ok = True
        for letter in yellow_letters:
            if letter not in word:
                ok = False
        if ok:
            ok_words_3.append(word)

    curr_guess = get_next_guess(ok_words_3, curr_guess)
    if curr_guess in words_remaining:
        words_remaining.remove(curr_guess)
    print("next guess:", curr_guess)
    print("guess_count:", guess_count)
    # TODO: switch to a green_letters comparison, not actual_word
    if curr_guess == actual_word:
        print("solved?:", curr_guess)
        break

im =Image.open("STEVE_THE_GOBLIN.JPG")
im.show()
