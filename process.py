# with open("./wordsToSearch/allWordsInEnglish.txt", "r") as f:
#     allWords = f.read().split("\n")

# for word in allWords:
#     if len(word) >= 4 and len(word) <= 10 and word.isalpha() and word.islower():

#         with open("./out/allPossibleWordsCombined.txt", "a") as f:
#             f.write(f"{word}\n")
import time
import datetime
from helpers import clear
with open("./out/allPossibleWordsCombined.txt", "r") as f:
    allWords = f.read().split("\n")

with open("./out/allLinks.txt", "r") as f:
    links = f.read().split("\n")

t1 = time.time()

longestWordLen = 0
longestWord = ""

for i, link in enumerate(links):
    clear()
    print(f"{i} / {len(links)} links checked")
    print(f"Total time processing: {datetime.timedelta(seconds=round(time.time() - t1, 0))}")
    print(
        f"Estimated time remaining: {datetime.timedelta(seconds=round(len(allWords) / round(time.time() - t1, 3), 0))}")
    print(f"Longest Word: {longestWordLen} - {longestWord}")
    for word in allWords:
        if len(word) >= 5 and len(word) <= 10:

            code = link[-12:]
            wholeLink = code.replace("-", "")

            if word in wholeLink:
                if len(word) > longestWordLen:
                    longestWordLen = len(word)
                    longestWord = word
                with open("./out/foundInWholeLink.txt", "a") as f:
                    f.write(f"{code} - {word}\n")
