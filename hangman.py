import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or '' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    while len(word_letters) > 0:
        print('YOu have used the letters', ' '.join(used_letter))
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('current word : ', ' '.join(word_list))

        user_letter = input("Guess a letter ").upper()
        if user_letter in alphabet - user_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letter:
            print("You already used that word")
        else:
            print("Invalid character")





user_input = input("type something")
print(user_input)