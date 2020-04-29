def text_analyzer(text=None):
    """This function counts the number of upper characters,
    lower characters, punctuation and spaces in a given text.
    If no argument is passed, the function prompts the user to
    enter an input text to analyze. If an empty text is passed,
    no analysis is done and a log message is printed.
    """
    if text is None:
        text = input("What is the text to analyze? ")
    if len(text) == 0:
        print("No text to analyze.")
    else:
        __parser(text)


def __parser(text):
    i = 0
    up = 0
    low = 0
    space = 0
    mark = 0
    for char in text:
        if char.isupper():
            up += 1
        elif char.islower():
            low += 1
        elif char.isspace():
            space += 1
        elif char.isprintable() and not char.isdigit():
            mark += 1
        i += 1
    print("The text contains " + str(i) + " characters.\n")
    print("- " + str(up) + " upper letters\n")
    print("- " + str(low) + " lower letters\n")
    print("- " + str(mark) + " punctuation marks\n")
    print("- " + str(space) + " spaces\n")
