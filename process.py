# with open("./wordsToSearch/allWordsInEnglish.txt", "r") as f:
#     allWords = f.read().split("\n")

# for word in allWords:
#     if len(word) >= 4 and len(word) <= 10 and word.isalpha() and word.islower():

#         with open("./out/allPossibleWordsCombined.txt", "a") as f:
#             f.write(f"{word}\n")
import time
import os
with open("./out/allPossibleWordsCombined.txt", "r") as f:
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

    clear()
    timePerLink = round(totalTime / i, 6)

    eta = round(timePerLink * (len(links) - i), 3)
    timeProcessing = round(totalTime, 3)

    print(f"{i} / {len(links)} links checked")
    print(f"{timePerLink}s per link")
    print(f"Total time processing: {timeProcessing}s")
    print(f"Estimated time remaining: {round(eta, 3)}s")
    print(f"Longest Word: {longestWordLen} - {longestWord}")
