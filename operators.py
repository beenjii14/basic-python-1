is_a_student = False
is_a_worker = True

# logical operators
# and
if is_a_student and is_a_worker:
    print("Is True")
else:
    print("Is False")

# or
if is_a_student or is_a_worker:
    print("Is True")
else:
    print("Is False")

# not
if not is_a_student:
    print("Is False")

# comparison operators
# are equal == 
number_one = '1'
number_two = 1
number_three = 1

if number_one == number_two:
    print('are equal')
else:
    print("aren't equal")

if number_one != number_three:
    print("True")
else:
    print("False")

if number_two > number_three:
    print("True")
else:
    print("False")
