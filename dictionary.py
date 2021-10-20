def main():
    my_dicitonary = {
        'name': 'Zed A. Shaw',
        'age': 35,
        'height': 74,
        'test': 'test'
    }
    print(my_dicitonary)
    print(my_dicitonary['name'])

    my_dicitonary['city'] = 'San Francisco'
    print(my_dicitonary)

    name = my_dicitonary.get('name') # get() method is used to get the value of a key
    nameNone = my_dicitonary.get('nameNone', None) # get() method is used to get the value of a key and if the key is not found, it will return None
    print(f'name: {name}')
    print(f'name none: {nameNone}')

    # del my_dicitonary['test'] # del() method is used to delete a key-value pair
    del my_dicitonary['test']
    print(my_dicitonary)

    my_dicitonary.pop('name') # pop() method is used to delete a key-value pair
    my_dicitonary.pop('name', None) # pop() method is used to delete a key-value pair and if the key is not found, it will return None
    print(my_dicitonary)

    if 'name' in my_dicitonary: # if the key is in the dictionary, it will return True
        print('name is in the dictionary')
    else:
        print('name is not in the dictionary')

    for key, value in my_dicitonary.items():
        print(key, value)

    for key in my_dicitonary.keys():
        print(key)
    
    for value in my_dicitonary.values():
        print(value)

if __name__ == '__main__':
    main()
