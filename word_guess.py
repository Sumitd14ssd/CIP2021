"""
File: word_guess.py
-------------------
When the user plays 'Word Guess', the computer first selects a secret
word at random from a list built into the program. The program then
prints out a row of dashes—one for each letter in the secret word
and asks the user to guess a letter. If the user guesses a letter
that is in the word, the word is redisplayed with all instances
of that letter shown in the correct positions, along with any
letters correctly guessed on previous turns. If the letter does
not appear in the word, the user is charged with an incorrect guess.
The user keeps guessing letters until either (1) the user has
correctly guessed all the letters in the word or (2) the user
has made EIGHT incorrect guesses.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def find_occurrences(word: str, character: str) -> list:
    """
    This function finds all the occurrences of `character` in `word`
    and returns a list of all the indices

    :param word: The string in which the occurrences are to be found
    :param character: The letter whose occurrences are to be found
    :return: A list of indices of 'character' in 'word'
    """
    return [i for i, letter in enumerate(word) if letter == character]


def play_game(secret_word: str) -> None:
    """
    Function first prints dashes instead of the `secret word`.
    No. of dashes equals no of letters in the words.

    :param secret_word: The word user has to guess
    """
    guessed_word = "".join('-' for letter in secret_word.strip())
    left_guesses = INITIAL_GUESSES
    while left_guesses > 0 and guessed_word != secret_word:
        print('The word now looks like this: {}'.format(guessed_word))
        print('You have {} guesses left'.format(left_guesses))

        letter_guess = input('Type a single letter here, then press enter: ').upper()
        if len(letter_guess) > 1:
            print('Guess should only be a single character.')
            continue
        indices = find_occurrences(secret_word, letter_guess)
        if len(indices) == 0:
            print("There are no {}'s in the word".format(letter_guess))
            left_guesses -= 1
        else:
            print('That guess is correct.')
            for i in range(len(indices)):
                letter_list = list(guessed_word)
                letter_list[indices[i]] = letter_guess
                guessed_word = ''.join(letter_list)
    
    if left_guesses == 0 or guessed_word != secret_word:
        print('Sorry, you lost. The secret word was: {}'.format(secret_word))
    else:
        print('Congratulations, the word is: {}'.format(secret_word))


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game. This function initially selects a word
    from a list by reading a list of words from the file specified
    by the constant LEXICON_FILE.
    """
    with open(LEXICON_FILE) as f:
        for line in f:
            word_list = f.readlines()

    index = random.randrange(len(word_list))

    return word_list[index]


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """

    print('=' * 40)
    print()
    print('Welcome to WORD GUESS!')
    print()
    print('=' * 40)

    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
