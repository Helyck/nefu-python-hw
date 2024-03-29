def get_three_sum(nums, target):
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return [i, j, k]
    return None


if __name__ == '__main__':
    print(get_three_sum([2, 7, 11, 15], 24))
    print(get_three_sum([2, 7, 11, 15], 33))
    print(get_three_sum([2, 7, 11, 15], 100))
