def get_digit_sum(n):
    a = n
    s = 0
    while a > 0:
        remainder = a % 10
        s += remainder
        a = (a - remainder) / 10

    return s


if __name__ == '__main__':
    i = int(input("Num: "))
    print(get_digit_sum(i))
