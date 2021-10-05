def is_prime(number):
    if number % 1 != 0 and number % number != 0:
        return True
    else:
        return False


def main():
    number = int(input('enter number: '))
    if is_prime(number):
        print(f'Is prime')
    else:
        print('not prime')


if __name__ == '__main__':
    main()
