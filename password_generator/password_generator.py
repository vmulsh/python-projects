#Password Generator Project
#Viktor Mulishov

import random
import string

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_', '?', '@']


def get_number(comment: str):
    retries = 6
    for attempt in range(1, retries):
        try:
            return int(input(comment))
        except ValueError:
            print(f"Cannot convert the string to an integer, number of retries left {retries - attempt - 1}")
        except Exception as e:
            print(f"Unexpected error: {e.message}, type: {type(e)}, number of retries left {retries - attempt - 1}")

    print(f"Exiting due to the wrong input supplied")
    exit()


def generate_password(nr_letters: int, nr_symbols: int, nr_numbers: int):

    generated_pool = []  # to build a list of randomly chosen letters, symbols, numbers

    for letter in range(1, nr_letters+1):
        generated_pool.append(random.SystemRandom().choice(string.ascii_letters))

    for symbol in range(1, nr_symbols+1):
        generated_pool.append(random.SystemRandom().choice(symbols))

    for number in range(1, nr_numbers+1):
        generated_pool.append(random.SystemRandom().choice(string.digits))

    for i in range(random.SystemRandom().randint(2, 5)):
        random.SystemRandom().shuffle(generated_pool)

    return "".join(generated_pool)


if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")
    print(f"Symbols to be used are: {symbols}")

    nr_letters = get_number("How many letters would you like in your password?\n")
    nr_symbols = get_number(f"How many symbols would you like?\n")
    nr_numbers = get_number(f"How many numbers would you like?\n")

    print("The generated password:")
    print(generate_password(nr_letters, nr_symbols, nr_numbers))


