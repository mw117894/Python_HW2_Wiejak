import re
def countWords(path):
    with open(path, "r") as f:
        text = f.read()

    wordsCount = {}

    for word in re.findall("\w+",text):
        word = word.lower()
        if word in wordsCount.keys():
            wordsCount[word] += 1
        else:
            wordsCount[word] = 1

    print("wordsCount: " + wordsCount.__str__())

countWords("unprocessed_text")


