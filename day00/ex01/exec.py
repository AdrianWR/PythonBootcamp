#!/usr/bin/python3
import sys


def main():
    s = ' '.join(sys.argv[1::])
    s = s.swapcase()[::-1]
    print(s)


if __name__ == "__main__":
    main()
