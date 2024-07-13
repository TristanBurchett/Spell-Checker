yourWord = input("Enter a word: ")
wordNoErrors = False

def percentageOfWordCorrect(possibleWord, word):
    count = 0
    for i in range(min(len(possibleWord), len(yourWord))):
        if (possibleWord[i] == yourWord[i]):
            count+=1
    return (count/len(word))*100

def spellCheckWord(word):
    lengthCheckWords = []  # length the same or +- 1
    with open(#path to list of words) as file:
        # length check
        for line in file:
            line = line.strip()
            if len(line) == len(word):
                lengthCheckWords.append(line)
            if len(line) + 1 == len(word):
                lengthCheckWords.append(line)
            if len(line) - 1 == len(word):
                lengthCheckWords.append(line)
    # similar letters check
    letterCheckWords = []

    for possibleWord in lengthCheckWords:
        if percentageOfWordCorrect(possibleWord, word) > 80:
            letterCheckWords.append(possibleWord)
    print(letterCheckWords)

with open(#path to list of words) as file:
    for line in file:
        if yourWord == line.strip():
            wordNoErrors = True
            break
    wordNoErrors = False

if wordNoErrors:
    print("There were no errors.")

else:
    spellCheckWord(yourWord)
