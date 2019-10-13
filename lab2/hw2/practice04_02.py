def collatz_len(n):
    """Computes the length of the Collatz sequence starting at n."""
    collatz_seq = []
    add_collatz_element(collatz_seq, n)

    return len(collatz_seq)


def max_collatz_len(n):
    """Computes the longest Collatz sequence length for starting numbers less than n"""
    out = 0

    len_dict = {'1': 1, '2': 2}

    pass


def add_collatz_element(seq, n):
    seq.append(n)
    if n != 1:
        if n % 2 == 0:
            add_collatz_element(seq, n / 2)
        else:
            add_collatz_element(seq, 3 * n + 1)


print(collatz_len(13))  # => 10
print(max_collatz_len(1000))



# Challenge: Only attempt to solve these if you feel very comfortable with this material.
# print(max_collatz_len(1000000))
# print(max_collatz_len(100000000))