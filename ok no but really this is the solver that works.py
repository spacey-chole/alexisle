import pandas as pd
import random
import gamelogic

df = pd.read_csv("Word Lists.csv")
df = df[df["validWordleAnswer"].notna()]
word_list = df["validWordleAnswer"].tolist()
# print("wordList: ", word_list)

# actual_word = str(random.choices(word_list))
# have to remove the [' '] from the actual word. i hate the .choices method
# actual_word = actual_word[2: 7]
actual_word = "house"
# actual_word = "adieu"
print("actual_word: ", actual_word)

# TODO: find the smartest possible starting_word -- the one that always results in solving in 6 guesses
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
ok_words_4 = []

# TODO: edit the get_next_guess() method to pick a smarter guess so it gets it every time
#   first pick highest scoring, then from there pick most different ?
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


def get_next_guess(words_to_guess_from, prev_guess):
    # pick words that have the most letters than the first guess
    # highest_diff represents the maximum number of letters different from the original list are in the smart guesses
    highest_diff = 0
    diff = 0
    for i in range(len(words_to_guess_from)):
        poss_guess = words_to_guess_from[i]
        # print("poss_guess:", poss_guess)
        for j in range(len(prev_guess)):
            # print(" is", prev_guess[j], "in", poss_guess, "?")
            if prev_guess[j] not in poss_guess:
                # print(" no it isn't")
                diff += 1
                # print(" diff:", diff)
            # else:
            # print(" yes it is, do nothing")
        if diff > highest_diff:
            highest_diff = diff
            # max different letters from OG guess
            # print("highest_diff: ", diff)
        diff = 0
    # print("     highest_diff:", highest_diff)

    # now that we know the most possible letters we can differ, put the highest_diff words into a new list
    smarter_guesses = []
    for word in words_to_guess_from:
        poss_guess = word
        # print("poss_guess:", poss_guess)
        for letter in poss_guess:
            # print(" is", prev_guess[j], "in", poss_guess, "?")
            if letter not in poss_guess:
                # print(" no it isn't")
                diff += 1
                # print(" diff:", diff)
            # else:
            # print(" yes it is, do nothing")
        if diff == highest_diff:
            smarter_guesses.append(poss_guess)
        diff = 0
    # print("smarter guesses: ", smarter_guesses)
    # then, use the highest score based on letter frequency thing to pick the smartest of the smarter_guesses
    letterScores = {"e": 26, "a": 25, "r": 24, "i": 23, "o": 22, "t": 21, "n": 20, "s": 19, "l": 18, "c": 17,
                    "u": 16, "d": 15, "p": 14, "m": 13, "h": 12, "g": 11, "b": 10, "f": 9, "y": 8, "w": 7,
                    "k": 6, "v": 5, "x": 4, "z": 3, "j": 2, "q": 1}

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


words_remaining = [word for word in word_list]

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
    # print("sorting letters into the lists...")

    # TODO: make sure duplicate letters are properly added/removed from yellow list when they become green

    letter_colors = gamelogic.processGuess(curr_guess, actual_word)
    print(letter_colors)
    print("green_letters: ", green_letters)
    print("yellow_letters: ", yellow_letters)
    print("gray_letters: ", gray_letters)

    for c in range(len(letter_colors)):
        if letter_colors[c] == "green":
            green_letters[c] = curr_guess[c]
        elif letter_colors[c] == "yellow":
            yellow_letters.append(curr_guess[c])
        else:
            gray_letters.append(curr_guess[c])

    # now filtering the word list by deleting things that shouldn't be guessed because we know they're wrong
    # start by deleting based on gray letters
    # print("filtering by gray letters...")
    # print("before", len(words_remaining))
    for word in word_list:
        # curr_word = word_list[word]
        ok = True
        for letter in range(len(gray_letters)):
            if gray_letters[letter] in curr_word:
                ok = False
        if not ok and word in words_remaining:
            words_remaining.remove(word)

    # print("filtering by green letters...")
    for word in range(len(ok_words)):
        curr_word = ok_words[word]
        ok = True
        for letter in range(len(green_letters)):
            # print("curr_word", curr_word, "being checked for", green_letters[letter])
            if (curr_word[letter] != green_letters[letter]) and (green_letters[letter] != "_"):
                # print(curr_word, "doesn't have", green_letters[letter], "in the right spot. not ok.")
                ok = False
        if not ok and word in words_remaining:
            words_remaining.remove(word)

    # print("ok_words_2:", ok_words_2)
    # print("filtering by yellow letters...")
    # ok_words_2 to ok_words_3
    for word in words_remaining:
        ok = True
        for letter in yellow_letters:
            if letter not in word:
                ok = False
        if not ok and word in words_remaining:
            words_remaining.remove(word)

    # print("ok_words_3", ok_words_3)

    # prevents guessing the same thing more than once
    # for word in words_remaining:
    #     if word != curr_guess:
    #         words_remaining.append(word)

    # curr_guess = get_next_guess(ok_words_4, curr_guess)
    if 'FALSE' in words_remaining:
        words_remaining.remove('FALSE')
    curr_guess = get_next_guess(words_remaining, curr_guess)


    # picking next guess and incrementing guess_count
    guess_count += 1
    print("next guess:", curr_guess)
    print("guess_count:", guess_count)
    if curr_guess == actual_word:
        print("solved (on next guess):", curr_guess)
        break