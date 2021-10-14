import os


def counter(fname):
    num_words = 0
    num_lines = 0

    with open(fname, "r") as f:
        for line in f:
            line = line.strip(os.linesep)
            wordslist = line.split()
            num_lines = num_lines + 1
            num_words = num_words + len(wordslist)

    print("Number of words in text file: ", num_words)

    print("Number of lines in text file: ", num_lines)


print("Obama:")
counter("data\obama_speech.txt")
print()
print("Michelle Obama:")
counter("data\michelle_obama_speech.txt")
print()
print("Trump:")
counter("data\donald_speech.txt")
print()
print("Melania Trump:")
counter("data\melina_trump_speech.txt")
