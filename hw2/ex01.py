def number_of_matches(J, S):
    out = 0
    for c in S:
        if c in J:
            out += 1

    return out


if __name__ == '__main__':
    print(number_of_matches("aA", "aAAbbbb"))
    print(number_of_matches("z", "ZZ"))
