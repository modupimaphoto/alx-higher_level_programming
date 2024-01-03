#!/usr/bin/python3

def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    new_text = ''

    for char in text:
        new_text += char

        if char in punctuation:
            new_text += '\n\n'

    print(new_text.strip())
