text_file = open("words.txt", "r")
wordArray = text_file.read().split('\n')

actualWord = "which" #testing with this word
startingWord = "adieu"
currGuess =  startingWord;

correctLetters = ["","","","",""]

#this will be the for loop to check if the words finished
#while actualWord != "".join(correctLetters);

for l in range(len(currGuess)):
    if (l in actualWord):
        print(l)
