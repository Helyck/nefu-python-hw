def is_self_dividing(n):
    s = str(abs(n))

    if "0" in s:
        return False

    for digit in s:
        d = int(digit)
        if n % d != 0:
            return False

    return True


if __name__ == '__main__':
    i = int(input("Num: "))
    print(is_self_dividing(i))
