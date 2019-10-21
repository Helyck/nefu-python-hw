def get_partition(S):
    out = []
    beg = 0
    end = get_end_of_right_partition_started_at(S, 0)
    out.append(S[beg:end])
    while end < len(S) - 1:
        beg = end + 1
        end = get_end_of_right_partition_started_at(S, beg)
        out.append(S[beg:end])

    return out


def get_end_of_right_partition_started_at(s, beg):
    end = get_extreme_indexes_for_char(s, s[beg])[1]

    if end > beg:
        cursor = beg + 1
        while cursor < end:
            e = get_extreme_indexes_for_char(s, s[cursor])[1]
            if e > end:
                end = e
            cursor += 1

    return end


def get_extreme_indexes_for_char(s, c):
    end = -1
    beg = s.find(c)
    if beg != -1:
        end = beg
        for i in range(beg + 1, len(s)):
            if s[i] == c:
                end = i

    return [beg, end]


if __name__ == '__main__':
    print(get_partition("qbqbcbqcqdufugduhxjhklxj"))
