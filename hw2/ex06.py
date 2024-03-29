def get_two_sum(nums, target):
    # Решение через словарь не оптимально по памяти, потому что надо создавать словарь. Поэтому решение дважды
    # итерировать по списку не хуже (в общем случае).
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


if __name__ == '__main__':
    print(get_two_sum([2, 7, 11, 15], 9))
    print(get_two_sum([2, 7, 11, 15], 18))
    print(get_two_sum([2, 7, 11, 15], 100))
