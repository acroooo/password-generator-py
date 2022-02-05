import random
import string


def generate_password(lenght):
    password = []
    for i in range(lenght):
        password.append(random.choice(string.ascii_letters + string.digits +
                        string.punctuation + string.hexdigits + string.octdigits))
    return ''.join(password)


def gen():
    length_pass = int(input("How long do you want your password to be? "))
    password = generate_password(length_pass)
    print("Generating password...")
    print("Your password is: " + password)


if __name__ == '__main__':
    gen()
