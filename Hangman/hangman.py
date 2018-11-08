from random import choice

# Opening file for obtaining word for hangman gane
# School computer's personal dir is "C:\\Users\\kekalda\\Documents\\Proge\\harjutusulesanded\\Hangman\\words.txt"
with open("words.txt", "r", encoding="utf-8") as word_file:
    plain_words_list = []
    for line in word_file:
        plain_words_list.append(line.replace("\n", ""))

# Debug
plain_word = choice(plain_words_list)
print("\n", plain_word)
print("\n", plain_words_list)

# This function makes word suitable for hangman game (showing only on letter and others are replace with underline)

def one_lettering(chosen_word):

    one_letter_word = []

    for char in chosen_word:

        if char == chosen_word[0]:
            one_letter_word.append(char)

        if char != chosen_word[0]:
            one_letter_word.append(" _ ")

    return "".join(one_letter_word)


game_word = one_lettering(plain_word)
print("\n", game_word)

while True:
    user_offer = input("Please enter a letter: ")

    lives = 3

    guessed_word = []

    for char in plain_word:

        for user_offer in char:

            if char == user_offer:
                guessed_word.append("")
                print("You have guessed a letter!")

            if char != user_offer:
                lives -= 1
                print("This not a letter you are looking for!")

    break
