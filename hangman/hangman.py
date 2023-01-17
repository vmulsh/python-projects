from hangman_art import logo
from hangman_art import stages
from hangman_words import words_pool
import random

current_state = []
letters_guessed = []


def guess_letter():
    global letters_guessed

    while True:
        letter = input("Guess a letter: ").strip()
        if not (len(letter) == 1 and letter.isalpha()):
            print(f"Wrong input - {letter}, ONE LETTER is needed, try again")
            continue
        if letter.lower() in letters_guessed:
            print(f"You already tried to guess the letter {letter}, try again")
            continue

        letters_guessed.append(letter.lower())

    return letter.lower()


def main():
    print(logo)
    print(stages[-1], end='\r')

    guessed_word = random.choice(words_pool)

    for item in guessed_word:
        current_state.append('_')

    print(' '.join(current_state))

main()