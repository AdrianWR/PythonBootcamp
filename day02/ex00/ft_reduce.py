#!/usr/bin/python3


def ft_reduce(function_to_apply, list_of_inputs):
    f = function_to_apply
    lst = list_of_inputs
    size = len(lst) - 1
    i = 1
    result = f(lst[0], lst[i])
    while (i < size):
        i += 1
        result = f(result, lst[i])
    return result


if __name__ == "__main__":

    def ft_sum(x, y):
        return x + y

    s = range(3, 7)
    r = ft_reduce(ft_sum, s)
    print(r)
