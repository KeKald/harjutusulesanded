# Checking if user inputed word is DNA or not


def dna_check(input):

    global dna_char

    for char in input:

        if char in dna_char:

            return True

# Giving feedback if user inserted word is DNA or not


def feedback(a):

    if a == True:
        print("\nThis word is a DNA!")

    else:
        print("\nThis word is not a DNA")


dna_char = ["a", "t", "c", "g"]

user_input = str(input("\nPlease enter a random word: ")).lower()
answer = dna_check(user_input)
feedback(answer)
