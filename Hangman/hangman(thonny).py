from random import choice

# Opening file for obtaining word for hangman gane
# School computer's personal dir is "C:\\Users\\kekalda\\Documents\\Proge\\harjutusulesanded\\Hangman\\words.txt"
with open("words.txt", "r", encoding="utf-8") as word_file:
    plain_words_list = []
    for line in word_file:
        plain_words_list.append(line.replace("\n", ""))

# This function makes word suitable for hangman game (showing only on letter and others are replace with underline)
def one_lettering(chosen_word):

    one_letter_word = []

    for char in chosen_word:

        if char == chosen_word[0]:
            one_letter_word.append(char)

        if char != chosen_word[0]:
            one_letter_word.append(" _ ")

    return "".join(one_letter_word)

# This function checks if there user inserted letter is in a game word
def letter_control():
    global plain_word
    global user_offer

    if user_offer == plain_word[order]:
        print("User_offer was in a word")
        return True
    
    if user_offer != plain_word[order]:
        print("User_offer wasn't in a word")
        return False

# This function checks if there is an 0 or 1 in a array and after that acts acordingly
def bit_check():
    global bit_word
    global order
    
    for order in range(len(bit_word)):
        
        if bit_word[order] == 0:

            if letter_control():
                bit_word[order] = 1
                
def bit_to_word():
    global bit_word
    global plain_word
    
    for sequence in range(len(bit_word)):
        
        if bit_word[sequence] == 0:
            bit_word[sequence] = " _ "
            
        if bit_word[sequence] == 1:
            bit_word[sequence] = plain_word[sequence]
            
    return print("".join(bit_word))
def word_to_bit():
    global bit_word
    global plain_word
    
    for sequence in range(len(bit_word)):
        
        if bit_word[sequence] == " _ ":
            bit_word[sequence] = 0
            
        if bit_word[sequence] == str():
            bit_word[sequence] = 1

plain_word = choice(plain_words_list)
game_word = one_lettering(plain_word)

# Debug
#print("\n", game_word)
#print("\n", plain_word)
#print("\n", plain_words_list)


bit_word = [1]
for a in range(len(plain_word) - 1):
    bit_word.append(int(0))

while True:
    user_offer = input("Please enter a letter: ")
    lives = 3
    
    # Debug    
    #print("\n", plain_word)
    print(bit_word)

    bit_check()
    bit_to_word()
    word_to_bit()

