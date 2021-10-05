def palindrome(word):
    word = word.strip().replace(' ', '').lower()
    if word[::] == word[::-1]:
        return True
    else:
        return False


def main():
    word = input('Enter you word: ')
    is_palindrome = palindrome(word)
    if is_palindrome:
        print('Is palindrome')
    else:
        print('Not palindrome')


if __name__ == '__main__':
    main()
