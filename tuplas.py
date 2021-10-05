numbers = [1,2,3,4,5]
number2 = [6,7,8,9]


final_numbers = numbers + number2
print(final_numbers)


my_tupla = (1,2,3,4,5)
# Tuples are static data types, their content cannot be modified. (inmutable)
# error
# my_tupla.append(6)

for number in my_tupla:
    print(number)
