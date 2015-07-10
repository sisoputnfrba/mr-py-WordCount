#! /usr/bin/python2
import sys

acumulator = 0
old_key = None

for token in sys.stdin.readlines():

    word = token.split()[0]
    repetitions = int(token.split()[1])

    if old_key is None:
        old_key = word

    if old_key != word:
        sys.stdout.write(old_key + " " + str(acumulator) + "\n")
        acumulator = 0
        old_key = word

    acumulator += repetitions

sys.stdout.write(old_key + " " + str(acumulator) + "\n")
