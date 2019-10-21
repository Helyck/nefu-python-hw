def is_valid(braces_string):
    count = 0  # non closed bracket count
    for c in braces_string:
        if c == '(':
            count += 1
        if c == ')':
            count -= 1
            if count < 0:
                return False

    if count == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_valid("()"))
    print(is_valid("("))
    print(is_valid("()()"))
    print(is_valid("(()("))
    print(is_valid("())("))
