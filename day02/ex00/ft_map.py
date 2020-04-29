#!/usr/bin/python3


class ft_map(object):
    def __init__(self, function_to_apply, list_of_inputs):
        self.f = function_to_apply
        self.lst = list_of_inputs
        self.gen = (self.f(i) for i in self.lst)
    pass

    def __iter__(self):
        return self.gen

    def __next__(self):
        return next(self.gen)


if __name__ == "__main__":
    s = 'apple'
    x = ft_map(str.upper, s)
    print(list(x))
