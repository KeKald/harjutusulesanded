import string


def input_control():

    global user_input

    if user_input.isdigit() == True:

        return False

    return True

def one_letter_forward(input, alphabet):

    for char in range(len(input)):

        letter_place_in_alphabet = alphabet.index(input[char])
        input = list(input)
        input[char] = alphabet[letter_place_in_alphabet + 1]

    return "".join(input)


while True:

    user_input = input("Please enter a random word: ").lower()

    correct_input = input_control()

    if correct_input == False:

        print("\nYou inserted a number!")

    if correct_input == True:

        break

alphabet = list(string.ascii_lowercase)

result = one_letter_forward(user_input, alphabet)
print(result)