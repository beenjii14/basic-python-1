import random


CAPITAL_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
LOWERCASE_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
CHARACTERS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

ALL_CHARACTERS = CAPITAL_LETTERS + LOWERCASE_LETTERS + NUMBERS + CHARACTERS


def password_generator():
    password = []
    for i in range(15):
        character_random = random.choice(ALL_CHARACTERS)
        password.append(character_random)

    return ''.join(password)


def main():
    password = password_generator()
    print(f'Your password is: {password}')


if __name__ == '__main__':
    main()
