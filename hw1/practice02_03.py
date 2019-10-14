def is_power_of_two(n):
    a = n

    if a <= 1:
        return False

    while a % 2 == 0:
        a = a / 2
        if a == 2:
            return True

    return False


if __name__ == '__main__':
    i = int(input("Num: "))
    print(is_power_of_two(i))
