def get_largest_perimiter(L):
    result = 0.0
    n = len(L)

    if n < 3:
        return 0

    for i1 in range(0, n - 2):
        for i2 in range(i1 + 1, n - 1):
            for i3 in range(i2 + 1, n):
                a = L[i1]
                b = L[i2]
                c = L[i3]
                if is_correct_triangle(a, b, c):
                    p = a + b + c
                    if result < p:
                        result = p

    return result


def is_correct_triangle(a, b, c):
    if a + b <= c:
        return False

    if a + c <= b:
        return False

    if b + c <= a:
        return False

    return True


if __name__ == '__main__':
    print(get_largest_perimiter([0, 1.5, 3.4, 2.1, 2.4]))
    print(get_largest_perimiter([3.4, 2.1]))
    print(get_largest_perimiter([100, 150, 180]))