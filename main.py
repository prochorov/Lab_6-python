import argparse
import secrets
import string


class Password:
    def __init__(self, set_):
        self.sets = set_

    def generate(self, length):
        password = ''
        while len(password) < length:
            set_ = secrets.choice(self.sets)
            char = secrets.choice(set_)
            password += char
        return password


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num_passwords', type=int, default=1, help='number of passwords to generate')
    parser.add_argument('-l', '--password_length', type=int, default=10, help='length of generated passwords')
    parser.add_argument('-a', '--alphabet', type=str, default='all', help='alphabet to use for generating passwords')
    args = parser.parse_args()

    num_passwords = args.num_passwords
    password_length = args.password_length
    alphabet = args.alphabet

    if alphabet == 'all':
        alphabet = string.ascii_letters + string.digits
    elif alphabet == 'ascii_lowercase':
        alphabet = string.ascii_lowercase
    elif alphabet == 'ascii_uppercase':
        alphabet = string.ascii_uppercase
    elif alphabet == 'digits':
        alphabet = string.digits

    password_generator = Password(alphabet)

    for i in range(num_passwords):
        password = password_generator.generate(password_length)
        print(password)


if __name__ == '__main__':
    main()
