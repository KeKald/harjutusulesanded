from random import choice

# Opening words text file for obtaining all words for the hangman game
with open("words.txt", "r", encoding="utf-8") as word_file:
    chosen_words_list = []
    for line in word_file:
        chosen_words_list.append(line.replace("\n", ""))

# This function checks if user inserted letter is in a selected word


def letter_control():

    global chosen_word
    global user_offer

    if user_offer == chosen_word[order]:
        return True

    if user_offer != chosen_word[order]:
        return False

# This function checks if there is an 0 or 1 in a array and with letter_control() function it makes changes in bits.
# 0 = not guessed and 1 = guessed or already there


def bit_check():

    global bit_word
    global order

    for order in range(len(bit_word)):

        if bit_word[order] == 0:

            if letter_control():

                bit_word[order] = 1

# Transferring 0's and 1's to chosen word


def bit_to_word():

    global bit_word
    global chosen_word

    for sequence in range(len(bit_word)):

        if bit_word[sequence] == 0:

            bit_word[sequence] = " _ "

        if bit_word[sequence] == 1:

            bit_word[sequence] = chosen_word[sequence]

    return print("\n", "".join(bit_word))

# Transferring chosen word letters to 0's and 1's


def word_to_bit():

    global bit_word
    global chosen_word

    for sequence in range(len(bit_word)):

        if bit_word[sequence] == " _ ":

            bit_word[sequence] = 0

        if bit_word[sequence] == str():

            bit_word[sequence] = 1

# Creating a list which will be used for controlling word and changing it to bits and letters.
# Array starts with chosen word's first letter and continues with appending 0 as long as list length equals with chosen word's letter count


def init_word_list():

    global bit_word
    global chosen_word

    bit_word = [chosen_word[0]]

    for a in range(len(chosen_word)):

        if a > 1:

            if chosen_word[a] == chosen_word[0]:

                bit_word.append(chosen_word[a])

        if chosen_word[a] != chosen_word[0]:

            bit_word.append(int(0))

# Printing out how good guess player had. Did player guess or not


def feedback_to_player():

    global bit_word
    global user_offer
    global lives
    global chosen_word

    guess = False

    for sequence in range(len(bit_word)):

        if user_offer == bit_word[sequence]:
            guess = True

    if guess == True:
        print("\nYou have guessed a letter!")

    if guess == False:

        lives -= 1
        print("\nTry again!")
        print("You have lost a life. Only {} lives left!".format(lives))

# Checking if user has guessed all the letters or not
# If all the words are guessed, game will end with victory text


def victory_check():

    global bit_word
    global victory

    victory = True

    for sequence in range(len(bit_word)):

        if bit_word[sequence] == 0:

            victory = False

# Checks if user inserted word is already guessed or is it already shown


def letter_duplicate_check():

    global bit_word
    global user_offer

    for sequence in range(len(bit_word)):

        if user_offer == bit_word[sequence]:

            return True

    return False

# Checks if number has inserted a number


def input_number_check():

    global user_offer

    if user_offer.isdigit() == True:

        return True

    return False

# Checks if user has inserted more than one letter


def one_letter_input_check():

    global user_offer

    if len(user_offer) > 1:

        return True

    return False


# Game cycle

game_state = 0

while True:

    # Introduction and explanation for a player
    if game_state == 0:

        lives = 3

        print("Welcome to the hangman game!"
              "\n"
              "You just have to guess all letters from randomly selected word."
              "\n\n"
              "If you choose a letter correctly, you are one step close to a victory."
              "\n"
              "But"
              "\n"
              "If you offer a wrong letter, you will lose one life."
              "\n\n"
              "In total you have {} lives."
              "\n\n"
              "------------------------------------------------------".format(lives))

        game_state = 1

    # Initializing first variables and choosing a random word
    if game_state == 1:

        chosen_word = choice(chosen_words_list)
        init_word_list()

        print("\nYour first word starts with letter {}.\n".format(chosen_word[0]))

        bit_to_word()

        game_state = 2

    # Core gameplay
    if game_state == 2:

        while True:

            user_offer = str(input("\nPlease enter your guess: ")).lower()

            duplicate = False
            number = False
            over_one = False

            duplicate = letter_duplicate_check()
            number = input_number_check()
            over_one = one_letter_input_check()

            if duplicate == True:

                print("\nThis letter already exists in the word!")
                bit_to_word()

            if number == True:

                print("\nYour input consists of number(s)!")
                bit_to_word()

            if over_one == True:

                print("\nYou have entered more than 1 character!")
                bit_to_word()

            if duplicate == False and number == False and over_one == False:

                break

    word_to_bit()
    bit_check()
    victory_check()
    bit_to_word()
    feedback_to_player()
    word_to_bit()

    if victory == True:

        print("\nYou have guessed all the letters!")
        print("Congratulations!")
        print("You won!")

        break

    if lives == 0:

        print("\nYou have ran out of lives!")
        print("Maybe next time you are luckier.")

        break
