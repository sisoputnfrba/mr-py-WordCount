#! /usr/bin/python2
import sys
 
def clean(word):
    for symbol in ['\n', '\t', ',', '.', ',', '?', '-', '"', "'", '(', ')', "!", ";", ":"]:
        word = word.replace(symbol, '')
    return word.lower()
 
 
def print_words(words):
    for word in words:
    	if len(word) > 0:
        	sys.stdout.write(word+" 1\n")
 
content = sys.stdin.read()
words = content.split()
words = map(clean, words)
print_words(words)

