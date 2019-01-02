dance_moves = ['mashed potato', 'twist', 'washing machine', 'lawn mower', 'sprinkler', 'tootsie roll', 'electric slide']
numbers = [65, 22, 11, 31, 652, 44, 12, 5, 0, -11]

# .sort() mutates the original list
numbers.sort()
print(numbers)

# sorted returns an altered copy
sorted_by_length = sorted(dance_moves, key=len)

print(sorted_by_length)


fruit = "banana"
print(fruit[2:5])


# we may be tempted to do
# i = 1
# for value in numbers:
#     i += 1
collection = ["mango", "banana", "guava"]
mapping = {}
for i, v in enumerate(collection):
    mapping[v] = i

print(mapping)