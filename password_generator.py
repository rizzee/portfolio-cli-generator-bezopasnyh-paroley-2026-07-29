import argparse
import random
import string


def generate_password(length, char_set):
    if char_set == 'letters':
        chars = string.ascii_letters
    elif char_set == 'numbers':
        chars = string.digits
    else:
        chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description='Generate a secure password.')
    parser.add_argument('length', type=int, help='Length of the password')
    parser.add_argument('--chars', choices=['letters', 'numbers', 'mixed'], default='mixed',
                        help='Character set for the password (letters, numbers, mixed)')
    args = parser.parse_args()

    password = generate_password(args.length, args.chars)
    print(password)


if __name__ == '__main__':
    main()