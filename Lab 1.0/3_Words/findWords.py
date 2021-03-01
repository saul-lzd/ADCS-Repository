# Program: Count the number of occurrences for the given words passed as arguments
# author: Saul DLD

import sys


def main():
    words = dict.fromkeys({}, 0)
    args = readArgs()
    text = readFile()

    for w in args:
        words[w] = 0

    for w in args:
        match = True
        while match:
            if text.find(w) >= 0:
                text = text.replace(w, "-", 1)
                words[w] = words[w]+1
            else:
                match = False

    # print(text)
    print(words)


def formatText(txt):
    return


def readArgs():
    args = sys.argv
    if len(args) > 0:
        args.pop(0)
        return args
    else:
        raise Exception("No arguments provided")


def readFile():
    file = open("simple.txt", "r")
    return file.read()


if __name__ == "__main__":
    main()
