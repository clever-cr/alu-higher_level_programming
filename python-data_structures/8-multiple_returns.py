#!/usr/bin/python3
def multiplw_retuns(sentence):
    if sentence:
        length = len(sentence)
        letter1 = sentence[0]
    else:
        length = 0
        letter1 = None
    return tuple((length, letter1))
