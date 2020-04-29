import sys
import re


code = {'A': '.-',      'B': '-...',    'C': '-.-.',
        'D': '-..',     'E': '.',       'F': '..-.',
        'G': '--.',     'H': '....',    'I': '..',
        'J': '.---',    'K': '-.-',     'L': '.-..',
        'M': '--',      'N': '-.',      'O': '---',
        'P': '.--.',    'Q': '--.-',    'R': '.-.',
        'S': '...',     'T': '-',       'U': '..-',
        'V': '...-',    'W': '.--',     'X': '-..-',
        'Y': '-.--',    'Z': '--..',
        '0': '-----',   '1': '.----',   '2': '..---',
        '3': '...--',   '4': '....-',   '5': '.....',
        '6': '-....',   '7': '--...',   '8': '---..',
        '9': '----.',   ' ': ' / '}


def atomorse(s):
    try:
        s = ' '.join(s)             # Handle multiple args
        s = ' '.join(s.split())     # Trim aditional spaces
        s = ' '.join([code[i.upper()] for i in s])
    except KeyError:
        s = "ERROR"
    return s


def main():
    print(atomorse(sys.argv[1::]))


if __name__ == "__main__":
    main()
