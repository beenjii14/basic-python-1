import random


def main():
    number_random = random.randint(1, 100)
    while True:
        number_user = int(input('Ingresa un numero entre el 1 y el 100: '))
        if number_user < number_random:
            print('Ingresa un numero mayor')
        elif number_user > number_random:
            print('Ingresa un numero menor')
        else:
            print('Ganaste')
            break


if __name__ == '__main__':
    main()
