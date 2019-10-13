

def fizzbuzz(n):
    """Returns the sum of all numbers less than n divisible by 3 or 5."""
    out = 0
    for i in range(n):
        if i % 3 == 0:
            out += i
        elif i % 5 == 0:
            out += i

    return out


print(fizzbuzz(41))  # => 408
print(fizzbuzz(1001))
