import pandas as pd
import random
import gamelogic

df = pd.read_csv("Word Lists.csv")
df = df[df["validWordleAnswer"].notna()]
word_list = df["validWordleAnswer"].tolist()

# for producing guess
letterScores = {"e": 26, "a": 25, "r": 24, "i": 23, "o": 22, "t": 21, "n": 20, "s": 19, "l": 18, "c": 17,
                "u": 16, "d": 15, "p": 14, "m": 13, "h": 12, "g": 11, "b": 10, "f": 9, "y": 8, "w": 7,
                "k": 6, "v": 5, "x": 4, "z": 3, "j": 2, "q": 1}

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


green_letters = []
yellow_letters = {}
gray_letters = []
words_remaining = []
actual_word = word_list[random.randint(0, len(word_list))]


guess_count = 0


def setup():
    global guess_count

    guess_count = 0
    green_letters.clear()
    for i in range(5):
        green_letters.append("_")
    for letter in letterScores:
        yellow_letters[letter] = []
    gray_letters.clear()
    words_remaining.clear()
    for word in word_list:
        words_remaining.append(word)


def produce_guess():
    global green_letters
    global yellow_letters
    global gray_letters
    global words_remaining
    global actual_word
    global guess_count
    global curr_guess

    if guess_count == 0:
        curr_guess = "crane"
    elif guess_count == 1:
        curr_guess = "shtik"
    elif guess_count == 2:
        curr_guess = "mould"
    else:
        curr_guess = get_next_guess(words_remaining, curr_guess)

    print("guess", guess_count + 1, "-", curr_guess)

    letter_colors = gamelogic.processGuess(curr_guess, actual_word)

    for c in range(len(letter_colors)):
        if letter_colors[c] == "green":
            green_letters[c] = curr_guess[c]
        elif letter_colors[c] == "yellow":
            yellow_letters[curr_guess[c]].append(c)
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
            if len(yellow_letters[letter]) > 0 and letter not in words_remaining[i]:
                valid = False
        if not valid:
            del words_remaining[i]
        else:
            i += 1

    # filter out words with yellow letters in guessed positions
    for letter in yellow_letters:
        for j in range (len(yellow_letters[letter])):
            i = 0
            while i < len(words_remaining):
                if words_remaining[i][yellow_letters[letter][j]] == letter:
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
    return [letter for letter in curr_guess], letter_colors




def test_all_words():
    global actual_word
    incomplete_words = "didn't complete:"
    finished = 0

    for a in range(len(word_list)):
        print(a + 1, "of", len(word_list))
        setup()
        actual_word = word_list[a]
        print("actual -", actual_word)

        dnf = True
        while guess_count < 6:

            produce_guess()

            if curr_guess == actual_word:
                print("solved on guess", guess_count)
                finished += 1
                dnf = False
                break

        if dnf:
            print()
            print("didn't finish")
            incomplete_words += "\n#" + str(a+1) + " - " + actual_word

        print()
        print("------------------")

    print("Finished", finished, "out of", len(word_list), "within 6 guesses")
    print("Accuracy:", (finished / len(word_list)))
    print()
    print(incomplete_words)


# test_all_words()

