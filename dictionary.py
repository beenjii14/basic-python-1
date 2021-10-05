def main():
    my_dicitonary = {
        'name': 'Zed A. Shaw',
        'age': 35,
        'height': 74
    }
    print(my_dicitonary)
    print(my_dicitonary['name'])

    my_dicitonary['city'] = 'San Francisco'
    print(my_dicitonary)

    for key, value in my_dicitonary.items():
        print(key, value)

    for key in my_dicitonary.keys():
        print(key)
    
    for value in my_dicitonary.values():
        print(value)

if __name__ == '__main__':
    main()
