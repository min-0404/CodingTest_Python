from collections import defaultdict
from this import s

def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0;
        counter[letter] += 1;
    return counter

def countLetters2(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter, 0 );
        counter[letter] += 1;
    return counter;

def countLetters(word):
    counter = defaultdict(int);
    for l in word:
        counter[l] += 1;
    return counter;

def groupwords(words):
    grouper = defaultdict(int);
    for word in words:
        length = len(word);
        grouper[length].append(word);
    
    