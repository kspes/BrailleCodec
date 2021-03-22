#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

# Braille unicode symbols taken from original script and https://www.piliapp.com/symbol/braille/
# Croatian braille: https://hr.wikipedia.org/wiki/Brailleevo_pismo
# Code first translates joint Croatian characters such as 'lj', 'nj', and 'dz', then converts to braille by the 
# 't' table below.

t = {
    'a': '⠁',
    'b': '⠃',
    'c': '⠉',
    'č': '⠡',
    'ć': '⠩',
    'd': '⠙',
    'ǆ': '⠻',
    'đ': '⠹',
    'e': '⠑',
    'f': '⠋',
    'g': '⠛',
    'h': '⠓',
    'i': '⠊',
    'j': '⠚',
    'k': '⠅',
    'l': '⠇',
    'ǉ': '⠣',
    'm': '⠍',
    'n': '⠝',
    'ǌ': '⠫',
    'o': '⠕',
    'p': '⠏',
    'q': '⠟',
    'r': '⠗',
    's': '⠎',
    'š': '⠱',
    't': '⠞',
    'u': '⠥',
    'v': '⠧',
    'w': '⠺',
    'x': '⠭',
    'y': '⠽',
    'z': '⠵',
    'ž': '⠮',

    'A': '⠠⠁',
    'B': '⠠⠃',
    'C': '⠠⠉',
    'Č': '⠠⠡',
    'Ć': '⠠⠩',
    'D': '⠠⠙',
    'Ǆ': '⠠⠻',
    'Đ': '⠠⠹',
    'E': '⠠⠑',
    'F': '⠠⠋',
    'G': '⠠⠛',
    'H': '⠠⠓',
    'I': '⠠⠊',
    'J': '⠠⠚',
    'K': '⠠⠅',
    'L': '⠠⠇',
    'Ǉ': '⠠⠣',
    'M': '⠠⠍',
    'N': '⠠⠝',
    'Ǌ': '⠠⠫',
    'O': '⠠⠕',
    'P': '⠠⠏',
    'Q': '⠠⠟',
    'R': '⠠⠗',
    'S': '⠠⠎',
    'Š': '⠠⠱',
    'T': '⠠⠞',
    'U': '⠠⠥',
    'V': '⠠⠧',
    'W': '⠠⠺',
    'X': '⠠⠭',
    'Y': '⠠⠽',
    'Z': '⠠⠵',
    'Ž': '⠠⠮',

    '1': '⠼⠁',
    '2': '⠼⠃',
    '3': '⠼⠉',
    '4': '⠼⠙',
    '5': '⠼⠑',
    '6': '⠼⠋',
    '7': '⠼⠛',
    '8': '⠼⠓',
    '9': '⠼⠊',
    '0': '⠼⠚',

    '.': '⠲',
    ',': '⠂',
    '!': '⠖',
    '(': '⠶',
    ')': '⠶',
    '-': '⠤',
    ' ': ' ',
    '\n': '\n',
    '\r': '\r',
}

concatTable = {
    'Lj': 'Ǉ',
    'LJ': 'Ǉ',
    'lJ': 'ǉ',
    'lj': 'ǉ',
    'Nj': 'Ǌ',
    'NJ': 'Ǌ',
    'nJ': 'ǌ',
    'nj': 'ǌ',
    'Dž': 'Ǆ',
    'DŽ': 'Ǆ',
    'dŽ': 'ǆ',
    'dž': 'ǆ',
}

if len(sys.argv) < 2:
    print("usage: braille_codec.py <Text to translate>")
    sys.exit(2)

inputText = u' '.join([i.decode('utf-8') for i in sys.argv[1:]])
text = ''

# First, concat joint characters
inputLen = len(inputText)
i = 0
while i < inputLen - 1:
    c = inputText[i]
    c2 = c + inputText[i + 1]
    try:
        match = concatTable[c2]
        text += match
        i += 2
    except KeyError:
        text += c
        i += 1 

#print(text)

# Next, convert to braille

braille = ''

i = 0
for c in text:
    try:
        braille += t[c]
    except KeyError:
        print("ERROR: Character '%s' not supported by Croatian braille" % c)
        sys.exit(1)
    i += 1

print(braille)
