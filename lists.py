numbers = [1, 3, 5, 8, 13, 21, 34, 55, 89]

mix = [1, "two", 3, "four", 5, "six", 8, "ten", True, False]

print(numbers[0])
print(mix[2])


# Add an element at the end
numbers.append(100)
print(numbers)


# Delete an element
mix.pop(1)
print(mix)


for element in mix:
    print(element)

print(mix[1:3])
print(mix[::-1])
