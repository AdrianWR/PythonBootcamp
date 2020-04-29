import sys


def main():
    if len(sys.argv) < 2:
        message = ""
    elif len(sys.argv) > 2 or not sys.argv[1].isdigit():
        message = "ERROR"
    else:
        n = int(sys.argv[1])
        if n == 0:
            message = "I'm Zero."
        elif n % 2 == 0:
            message = "I'm Even."
        else:
            message = "I'm Odd."
    print(message)


if __name__ == "__main__":
    main()
