def is_prime(n):
    if n < 2:
        return False

    result = True
    for a in range(2, n - 1):
        if n % a == 0:
            result = False

    return result


if __name__ == '__main__':
    i = int(input("Num: "))
    print(is_prime(i))
