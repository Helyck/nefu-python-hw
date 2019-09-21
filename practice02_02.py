import practice02_01


def is_beauty(n):
    s = practice02_01.get_digit_sum(n)
    remainder = n % s
    return remainder == 0


if __name__ == '__main__':
    i = int(input("Num: "))
    print(is_beauty(i))
