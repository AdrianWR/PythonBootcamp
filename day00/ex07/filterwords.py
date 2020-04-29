import sys
import re


class InputError(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == "__main__":
    try:
        if (len(sys.argv) != 3):
            raise InputError("ERROR")
        elif (sys.argv[1].isdigit()):
            raise InputError("ERROR")
        n = int(sys.argv[2])
        s = re.split(r'[^\w]+', sys.argv[1])
        s = [i for i in s if len(i) > n]
        print(s)
    except ValueError:
        print("ERROR")
    except InputError as e:
        print(e.message)
