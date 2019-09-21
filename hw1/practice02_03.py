def is_power_of_two(n):
    a = n
    s = 0
    run = True
    result = False

    if a <= 0:
        run = False

    while run:
        if a % 2 == 1:
            run = False
        else:
            a = a / 2
            if a == 2:
                result = True
                run = False

    return result


if __name__ == '__main__':
    i = int(input("Num: "))
    print(is_power_of_two(i))
