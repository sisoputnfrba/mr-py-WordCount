#! /usr/bin/python2
import sys
 
dictionary = {}
 
def add_word(token, repetitions):
    if dictionary.has_key(token):
        dictionary[token] += int(repetitions)
    else:
        dictionary[token] = int(repetitions)
 
def print_words():
    for word in dictionary:
        sys.stdout.write(word+" " +str(dictionary[word])+"\n")
 
 
for token in sys.stdin.readlines():
    word = token.split()[0]
    repetitions = token.split()[1]
    add_word(word, repetitions)
 
print_words()
