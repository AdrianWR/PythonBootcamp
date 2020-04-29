#!/usr/bin/python3


class ft_filter(object):
    def __init__(self, function_to_apply, list_of_inputs):
        self.f = function_to_apply
        self.lst = list_of_inputs
        self.gen = (i for i in self.lst if self.f(i) is True)
    pass

    def __iter__(self):
        return self.gen

    def __next__(self):
        return next(self.gen)


if __name__ == "__main__":
    s = 'a1p3p4l1e'
    f = ft_filter(str.isalpha, s)
    print(list(f))
