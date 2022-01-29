# with open("./wordsToSearch/allWordsInEnglish.txt", "r") as f:
#     allWords = f.read().split("\n")

# for word in allWords:
#     if len(word) >= 4 and len(word) <= 10 and word.isalpha() and word.islower():

#         with open("./out/allPossibleWordsCombined.txt", "a") as f:
#             f.write(f"{word}\n")
import time
import os
# with open("./out/allPossibleWordsCombined.txt", "r") as f:
#     allWords = f.read().split("\n")

with open("./wordsToSearch/1000CommonWords.txt", "r") as f:
    allWords = f.read().split("\n")

with open("./out/allLinks.txt", "r") as f:
    links = f.read().split("\n")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


longestWordLen = 0
longestWord = ""
totalTime = 0
print(len(links))

for i, link in enumerate(links, start=1):
    t1 = time.time()

    for word in allWords:
        if len(word) >= 5 and len(word) <= 10:
            code = link[-12:]
            wholeLink = code.replace("-", "")

            if word in wholeLink:
                if len(word) >= longestWordLen:
                    longestWordLen = len(word)
                    longestWord = word
                with open("./out/foundInWholeLink.txt", "a") as f:
                    f.write(f"{code} - {word}\n")

    seconds = time.time() - t1
    totalTime += seconds

    if i % 250 == 0:
        clear()
        timePerLink = round(totalTime / i, 6)

        eta = round(timePerLink * (len(links) - i), 3)
        minETA, secETA = divmod(round(eta, 3), 60)
        minProcessing, secProcessing = divmod(round(totalTime, 3), 60)

        print(f"{i} / {len(links)} links checked")
        print(f"{timePerLink}s per link")
        print(
            f"Total time processing: {round(minProcessing)}:{round(secProcessing)}")
        print(f"Estimated time remaining: {round(minETA)}:{round(secETA)}")
        print(f"Longest Word: {longestWordLen} - {longestWord}")
