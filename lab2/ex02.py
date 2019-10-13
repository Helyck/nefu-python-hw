def average(*args):
    """Return the average of numeric arguments or None if no arguments are supplied."""
    n = len(args)
    if n == 0:
        return

    s = 0.0
    for i in args:
        s += i

    return s / n


if __name__ == '__main__':
    print(average())
    print(average(5))
    print(average(6, 8, 9, 11))

    l = [3, 1, 41, 592, 65358]
    print(average(*l))
