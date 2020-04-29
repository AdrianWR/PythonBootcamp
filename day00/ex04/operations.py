#!/usr/bin/python3
import sys


class OperationError(Exception):
    """Default error class for exception handling
    in the operations.py program context. Contains
    help text and example in exception raise cases.
    """
    usage = "Usage: python " + sys.argv[0] + " <number1> <number2>"
    example = "Example:\n\tpython " + sys.argv[0] + " 10 3"
    help = usage + "\n" + example
    pass


class InputError(OperationError):
    """Exception class defined in context of error
    regarding strange inputs from the user when calling
    the program. This includes no argument passed,
    too many arguments or non-numeric arguments.
    """
    def __init__(self, message=None):
        self.message = type(self).__name__ + ": " + message + "\n\n"
        self.message += self.help
        pass


def main():
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        if len(sys.argv) > 3:
            raise InputError("Too many arguments.")
    except IndexError:
        error = OperationError
        print(error.help)
    except ValueError:
        error = InputError("Only numbers.")
        print(error.message)
    except InputError as error:
        print(error.message)
    else:
        __operation(a, b)


def __operation(a, b):
    try:
        print("Sum: ", a + b)
        print("Difference: ", a - b)
        print("Product: ", a * b)
        print("Quocient: ", a / b)
        print("Modulus: ", a % b)
    except ZeroDivisionError:
        print("ERROR (div by zero)")
        print("ERROR (modulo by zero)")


if __name__ == "__main__":
    main()
