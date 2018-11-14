
def input_control(input):

    if input.isdigit() == True:

        return False

    return True


def input_to_list(input):

    input = input.split(" ")

    return input


def sentence_to_dictionary(input):

    dictionary = {}

    for num in range(len(input)):

        if input[num] in dictionary:

            dictionary[input[num]] = dictionary.get(input[num]) + 1

        else:

            dictionary[input[num]] = 1

    return dictionary


while True:

    user_input = input("\nPlease enter a sentence: ").lower()
    correct_input = input_control(user_input)

    if correct_input == False:

        print("\nYou have entered a number(s)!")

    if correct_input == True:

        break

sentence_list = input_to_list(user_input)
dictionary = sentence_to_dictionary(sentence_list)

print("This sentence consists of these words with that many appearances:\n", dictionary)
