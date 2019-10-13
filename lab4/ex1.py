# Write `map` expressions to convert the following inputs into the indicated outputs.
# ['12', '-2', '0'] --> [12, -2, 0]

# ['hello', 'world'] --> [5, 5]

# ['hello', 'world']` --> ['olleh', 'dlrow']

# range(2, 6) --> [(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]

# zip(range(2, 5), range(3, 9, 2)) --> [6, 15, 28]


def string_reverse(x):
    return x[::-1]


print(list(map(int, ['12', '-2', '0'])))
print(list(map(len, ['hello', 'world'])))
print(list(map(string_reverse, ['hello', 'world'])))
print(list(map(lambda x: (x, x**2, x**3), range(2, 6))))
#print(list(map((lambda a, b: a * b), zip(range(2, 5), range(3, 9, 2)))))
print(list(map((lambda x: x[0] * x[1]), zip(range(2, 5), range(3, 9, 2)))))
