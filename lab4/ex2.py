# Write `filter` expressions to convert the following inputs into the indicated outputs.
# ['12', '-2', '0'] --> ['12', '0']

# ['hello', 'world'] --> ['world']

# ['Stanford', 'Cal', 'UCLA'] --> ['Stanford']

# range(20) --> [0, 3, 5, 6, 9, 10, 12, 15, 18]

result = filter(lambda x: x[0] != '-', ['12', '-2', '0'])
print(list(result))

result = filter(lambda x: x[0] != 'h', ['hello', 'world'])
print(list(result))

result = filter(lambda x: len(x) > 4, ['Stanford', 'Cal', 'UCLA'])
print(list(result))

result = filter(lambda x: x % 3 == 0 or x % 5 == 0, range(20))
print(list(result))
