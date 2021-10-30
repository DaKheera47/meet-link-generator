with open("./wordsToSearch/threeLetterWords.txt", "r") as f:
    threeWords = f.read().split("\n")

with open("./wordsToSearch/customThreeLetterWords.txt", "r") as f:
    customThreeWords = f.read().split("\n")

with open("./wordsToSearch/customFourLetterWords.txt", "r") as f:
    customFourWords = f.read().split("\n")

with open("./wordsToSearch/fourLetterWords.txt", "r") as f:
    fourWords = f.read().split(" ")

with open("./out/allLinks.txt", "r") as f:
    links = f.read().split("\n")

# making sure file starts out empty
with open("./out/foundLinks.txt", "w") as f:
    f.write("")

# writing all user defined threee letter words on the start or end of the link
with open("./out/foundLinks.txt", "a+") as f:
    f.write(f"Custom 3 letter combos\n")
i = 0
for link in list(set(links)):
    code = link[-12:]
    start = code[:3]
    mid = code[4:8]
    end = code[-3:]

    for word in list(set(customThreeWords)):
        if word == start or word == end:
            i += 1
            with open("./out/foundLinks.txt", "a+") as f:
                f.write(f"{link} -- custom 3 letter combo\n")
print(f"{i} custom three letter words found")

# writing all user defined four letter words in the middle of the link
with open("./out/foundLinks.txt", "a+") as f:
    f.write(f"\ncustomFourWords\n")
i = 0
for link in list(set(links)):
    code = link[-12:]
    start = code[:3]
    mid = code[4:8]
    end = code[-3:]

    for word in list(set(customFourWords)):
        if word == mid:
            i += 1
            with open("./out/foundLinks.txt", "a+") as f:
                f.write(f"{link} -- customFourWords\n")
print(f"{i} custom four letter words found")

# writing four letter words in the middle of the link
with open("./out/foundLinks.txt", "a+") as f:
    f.write(f"Middle\n")
i = 0
for link in list(set(links)):
    code = link[-12:]
    start = code[:3]
    mid = code[4:8]
    end = code[-3:]

    for word in list(set(fourWords)):
        if word == mid:
            i += 1
            with open("./out/foundLinks.txt", "a+") as f:
                f.write(f"{link} -- Middle\n")
print(f"{i} four letter words from dictionary found")

# writing three letter words at the start or end of link
with open("./out/foundLinks.txt", "a+") as f:
    f.write(f"Start\n")
i = 0
for link in list(set(links)):
    code = link[-12:]
    start = code[:3]
    mid = code[4:8]
    end = code[-3:]

    for word in list(set(threeWords)):
        if word == start:
            i += 1
            with open("./out/foundLinks.txt", "a+") as f:
                f.write(f"{link} -- Start\n")
print(f"{i} three letter words from dictionary found at the start of the link")

# writing three letter words at the end of link
with open("./out/foundLinks.txt", "a+") as f:
    f.write(f"End\n")
i = 0
for link in list(set(links)):
    code = link[-12:]
    start = code[:3]
    mid = code[4:8]
    end = code[-3:]

    for word in list(set(threeWords)):
        if word == end:
            i += 1
            with open("./out/foundLinks.txt", "a+") as f:
                f.write(f"{link} -- End\n")
print(f"{i} three letter words from dictionary found at the end of the link")
