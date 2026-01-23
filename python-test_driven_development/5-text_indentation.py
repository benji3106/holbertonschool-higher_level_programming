#!/usr/bin/python3
"""Module that prints a text with indentation."""


def text_indentation(text):
    """Prints a text with 2 new lines after
      each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    new_line = True

    while i < length:
        if new_line and text[i] == ' ':
            i += 1
            continue

        print(text[i], end='')
        new_line = False

        if text[i] in ['.', '?', ':']:
            print('\n')
            new_line = True
            while i + 1 < length and text[i + 1] == ' ':
                i += 1

        i += 1
