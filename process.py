# with open("./wordsToSearch/allWordsInEnglish.txt", "r") as f:
#     allWords = f.read().split("\n")

# for word in allWords:
#     if len(word) >= 4 and len(word) <= 10 and word.isalpha() and word.islower():

#         with open("./out/allPossibleWordsCombined.txt", "a") as f:
#             f.write(f"{word}\n")
import time
with open("./out/allPossibleWordsCombined.txt", "r") as f:
    allWords = f.read().split("\n")

with open("./out/allLinks.txt", "r") as f:
    links = f.read().split("\n")
t1 = time.time()
for word in allWords:
    for link in links:
        if len(word) >= 4 and len(word) <= 10:
            code = link[-12:]
            wholeLink = code.replace("-", "")
            if word in wholeLink:
                with open("./out/foundInWholeLink.txt", "a") as f:
                    f.write(f"{code} - {word}\n")

print(f"Processing time: {round(time.time() - t1, 3)}s")
