def example_one():
    for count in range(1000):
        print(count)


def example_two():
    for i in range(0, 100):
        print(f'2 elevado a {i} es igual a {2**i}')


def multiplication_table(table):
    for number in range(0, 11):
        print(f'{table} x {number} = {table*number}')


def multiplication_menu():
    while True:
        menu = """
    Bienvenido, que tabla de multiplicar deseas saber
    1.- Tabla del 1
    2.- Tabla del 2
    3.- Tabla del 3
    4.- Tabla del 4
    5.- Tabla del 5
    Elige una tabla de multiplicar: """
        table = int(input(menu))
        if table > 0 and table < 6:
            multiplication_table(table)
            break


def get_word():
    word = input('Enter your name: ')
    for character in word:
        print(character)


def main():
    # example_one()
    # example_one()
    # multiplication_menu()
    get_word()

if __name__ == '__main__':
    main()
