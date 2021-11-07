with open("./wordsToSearch/1000CommonWords.txt", "r") as f:
    allWords = f.read().split("\n")

for word in allWords:
    if len(word) == 3:
        with open("./wordsToSearch/common3Words.txt", "a") as f:
            f.write(f"{word}\n")
