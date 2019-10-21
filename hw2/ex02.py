def get_sorted_squares(nums):
    out = []
    for n in nums:
        out.append(n * n)
    out.sort()

    return out


if __name__ == '__main__':
    print(get_sorted_squares([-4, -1, 0, 3, 10]))
    print(get_sorted_squares([-7,-3,2,3,11]))
