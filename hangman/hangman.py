from hangman_art import logo
from hangman_art import stages
from hangman_words import words_pool
import random

current_state = []
letters_guessed = []


def guess_letter():
    global letters_guessed

    while True:
        letter = input("\nGuess a letter: ").strip()
        if not (len(letter) == 1 and letter.encode().isalpha()):  # encode() to filter non-English letters
            print(f'Wrong input "{letter}", ONE ENGLISH LETTER is needed, try again')
            continue
        if letter.lower() in letters_guessed:
            print(f'You already tried to guess the letter "{letter.lower()}", try again')
            continue

        letters_guessed.append(letter.lower())

        return letter.lower()


def check_guess(letter, word):
    global current_state

    if letter not in word:
        return False
    else:
        for pos, item in enumerate(word):
            if item == letter:
                current_state[pos] = letter
        return True


def main():
    try:
        print(logo)

        errors_count = 0  # maximum 6
        hidden_word = random.choice(words_pool)

        print(f'You are welcome! Try to guess the word!')
        print(' '.join(current_state))
        print(stages[-1 - errors_count])

        for item in hidden_word:
            current_state.append('_')

        while errors_count < 6:
            guess_attempt = guess_letter()
            guess_result = check_guess(guess_attempt, hidden_word)

            if guess_result:
                print(f'You guessed the letter "{guess_attempt}"!')
            else:
                errors_count += 1
                print(f'wrong letter "{guess_attempt}"! # of attempts left: {6 - errors_count}')
                print(stages[-1 - errors_count])

            print(' '.join(current_state))

            if '_' not in current_state:
                print(f'\nYou guessed the word "{hidden_word}"! Nice one!')
                break
            elif errors_count == 6:
                print(f'\nUnfortunately, you lost, the hidden word was "{hidden_word}"')
                break
    except Exception as e:
        print(f"Unexpected error: {e.message}, type: {type(e)}")


if __name__ == '__main__':
    main()
