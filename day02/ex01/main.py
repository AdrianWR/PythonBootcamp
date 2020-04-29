def what_are_the_vars(*args, **kwargs):
    """Your code"""""
    obj = ObjectC()
    for i in kwargs.keys():
        try:
            getattr(obj, i)
        except AttributeError:
            setattr(obj, i, kwargs[i])
        else:
            return None
    for i, j in enumerate(args):
        try:
            getattr(obj, f"var_{i}")
        except AttributeError:
            setattr(obj, f"var_{i}", j)
        else:
            return None
    return obj


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
