#!/usr/bin/pyhton3
"""defines text idetantation function"""


def text_indentation(text):
    """text indentation"""
    if type(text) == str:
        symbols = ':.?'
        for i in symbols:
            strings = []
            for k in text.split(i):
                strings.append(k.strip(" "))
            text = (i + "\n\n").join(strings)
        print(text, end="")
    else:
        raise TypeError('text must be a string')
