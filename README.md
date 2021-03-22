### Fork Note
This is a modifed version of the original script taken from: https://github.com/its-sarin/BrailleCodec.
The change is that it's adjusted to work with Croatian Braille instead of English.

# BrailleCodec
A small python script to encode plain text to Braille or decode Braille to plain text

### Usage

To encode a plain text string:
```sh
$ python braille_codec.py -e myname
$ ⠍⠽⠝⠁⠍⠑
```


To decode a Braille string:
```sh
$ python braille_codec.py -d ⠍⠽⠝⠁⠍⠑
$ myname
```

### What is the point of this?
Honestly Braille characters just look cool and have a sort of "cyberpunk" style to them when displayed on a screen. This otherwise serves no real world purpose for the blind.
