#!/usr/bin/python3.5

import random
import collections

words = []

with open("gettysburg.txt", "r") as f:
    words.append(f.read())

words[0] = words[0].lower()
words[0] = words[0].replace(".", "")
words[0] = words[0].replace("\n\n", " a ")
words[0] = words[0].replace("\n", "")
words[0] = words[0].replace("--", "a")
words[0] = words[0].replace("-", "")
words[0] = words[0].replace(",", "")

words = words[0].split(" ")

long_words = []
long_words_final = {}
myWordList = []

for word in words:
    if len(word) >= 5:
        long_words.append(word)

long_words_final = collections.Counter(long_words)

for key in long_words_final.keys():
    myWordList.append(key)

print(random.choice(myWordList))
