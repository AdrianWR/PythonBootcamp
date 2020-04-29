#!/usr/bin/python3

import os
import math
import requests


def generator(text, sep=" ", option=None):
    try:
        words = text.split(sep)
        if option == "shuffle":
            __shuffle(words)
        elif option == "unique":
            # Starting from Python 3.6+, dictionares are
            # insertion ordered.
            words = list(dict.fromkeys(words))
        elif option == "ordered":
            words.sort()
        elif option is not None:
            raise AttributeError
    except AttributeError:
        print("ERROR")
        yield None
    else:
        for i in words:
            yield i


# def __random_sequence_web(list_size):
#     """Gets random sequence of integers from HTTP request"""
#     website = f"https://random.org/sequences/?" + \
#               f"min=0&max={list_size}&" + \
#               f"col=1&format=plain&rnd=new"
#     r = requests.get(website)
#     return r.text.split()

def __shuffle(list):
    # Fisher-Yates Shuffle
    """Gets random sequence of integers from /dev/urandom UNIX device.

    This function is an implementation of the Durstenfeld version of
    the Fisher-Yates shuffle algorthm. To get the random indexes, it
    reads a certain number of bytes from /dev/urandom. As such, the
    behavior on non-Linux systems is unknown. To get a more precise
    randomness for long lists, it reads n bytes according to the list
    size (e.g. 1 byte readed for lists with less than 256 elements, 2 
    bytes for lists with less than 65536 elements, and so on). For more
    details regarding the algorithm, access its Wikipedia page: 
    https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    Space Complexity    -> O(1)
    Time Complexity     -> O(n)
    """
    list_size = len(list)
    n_bytes = math.ceil(math.log(list_size, 2) / 8)
    while list_size - 1:
        rand = int.from_bytes(os.urandom(n_bytes), "big") % list_size
        tmp = list[rand]
        list[rand] = list[list_size - 1]
        list[list_size - 1] = tmp
        list_size -= 1
    return list


def __print_generator(generator):
    for i in generator:
        if i:
            print(i)
    print("\n")


if __name__ == "__main__":
    text = "banana avocado apple pineapple blueberry cherry apple banana"
    print("NONE")
    __print_generator(generator(text))
    print("SHUFFLE")
    __print_generator(generator(text, option="shuffle"))
    print("ORDERED")
    __print_generator(generator(text, option="ordered"))
    print("UNIQUE")
    __print_generator(generator(text, option="unique"))
    print("ERROR CASE")
    __print_generator(generator(text, option="ghanasaysgoodbye"))
