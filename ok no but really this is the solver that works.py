import pandas as pd
import random
import gamelogic

df = pd.read_csv("Word Lists.csv")
df = df[df["validWordleAnswer"].notna()]
word_list = df["validWordleAnswer"].tolist()




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
    diverse_guesses = []
    for guess_word in words_to_guess_from:
        diff = 0
        for letter in prev_guess:
            if letter not in guess_word:
                diff += 1
        if diff > highest_diff:
            diverse_guesses.clear()
            highest_diff = diff
        if diff == highest_diff:
            diverse_guesses.append(guess_word)


    # then, use the highest score based on letter frequency thing to pick the smartest of the smarter_guesses
    letterScores = {"e": 26, "a": 25, "r": 24, "i": 23, "o": 22, "t": 21, "n": 20, "s": 19, "l": 18, "c": 17,
                    "u": 16, "d": 15, "p": 14, "m": 13, "h": 12, "g": 11, "b": 10, "f": 9, "y": 8, "w": 7,
                    "k": 6, "v": 5, "x": 4, "z": 3, "j": 2, "q": 1}

    highest_score = 0
    highest_word = ""
    for guess_word in diverse_guesses:
        score = 0
        for letter in guess_word:
            score += letterScores[letter]
        if score > highest_score:
            highest_score = score
            highest_word = guess_word

    return highest_word



finished = 0

for a in range(len(word_list)):
    print(a+1, "of", len(word_list))

    green_letters = ["_", "_", "_", "_", "_"]
    yellow_letters = []
    gray_letters = []

    words_remaining = [word for word in word_list]

    actual_word = "tweed"
    # actual_word = word_list[random.randint(0, len(word_list))]
    actual_word = word_list[a]

    print("actual -", actual_word)

    starting_word = "crane"

    curr_guess = starting_word

    guess_count = 0
    while guess_count < 6:

        print("guess", guess_count+1, "-", curr_guess)

        if curr_guess == actual_word:
            print("solved on guess", guess_count+1)
            finished += 1
            break


        letter_colors = gamelogic.processGuess(curr_guess, actual_word)

        for c in range(len(letter_colors)):
            if letter_colors[c] == "green":
                green_letters[c] = curr_guess[c]
            elif letter_colors[c] == "yellow":
                yellow_letters.append(curr_guess[c])
            else:
                gray_letters.append(curr_guess[c])

        # keep words with matching green letters
        i = 0
        while i < len(words_remaining):
            word = words_remaining[i]
            valid = True
            for j in range(len(green_letters)):
                if (word[j] != green_letters[j]) and (green_letters[j] != "_"):
                    valid = False
            if not valid:
                del words_remaining[i]
            else:
                i += 1

        # keep words with yellow letters
        i = 0
        while i < len(words_remaining):
            valid = True
            for letter in yellow_letters:
                if letter not in words_remaining[i]:
                    valid = False
            if not valid:
                del words_remaining[i]
            else:
                i += 1

        # filter by gray letters
        for j in range(len(letter_colors)):
            if letter_colors[j] == "gray":

                occurrences_in_guess = 0
                for k in range(len(letter_colors)):
                    if curr_guess[j] == curr_guess[k]:
                        if letter_colors[k] == "green" or letter_colors[k] == "yellow":
                            occurrences_in_guess += 1

                i = 0
                while i < len(words_remaining):
                    occurrences_in_word = 0
                    for h in words_remaining[i]:
                        if h == curr_guess[j]:
                            occurrences_in_word += 1

                    if occurrences_in_word > occurrences_in_guess:
                        del words_remaining[i]
                    else:
                        i += 1

        if curr_guess in words_remaining:
            words_remaining.remove(curr_guess)

        guess_count += 1

        curr_guess = get_next_guess(words_remaining, curr_guess)

        if guess_count == 1:
            curr_guess = "shtik"
        if guess_count == 2:
            curr_guess = "mould"




    if guess_count == 6:
        print()
        print("didn't finish")

    print()
    print("------------------")


print("Finished", finished, "out of", len(word_list), "within 6 guesses")
print("Accuracy:", (finished/len(word_list)))


