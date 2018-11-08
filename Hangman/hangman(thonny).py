from random import choice

# Opening file for obtaining word for hangman gane
# School computer's personal dir is "C:\\Users\\kekalda\\Documents\\Proge\\harjutusulesanded\\Hangman\\words.txt"
with open("words2.txt", "r", encoding="utf-8") as word_file:
    plain_words_list = []
    for line in word_file:
        plain_words_list.append(line.replace("\n", ""))

# This function checks if there user inserted letter is in a game word
def letter_control():
    global plain_word
    global user_offer

    if user_offer == plain_word[order]:
        return True
    
    if user_offer != plain_word[order]:
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
            
    return print("\n", "".join(bit_word))

def word_to_bit():
    global bit_word
    global plain_word
    
    for sequence in range(len(bit_word)):
        
        if bit_word[sequence] == " _ ":
            bit_word[sequence] = 0
            
        if bit_word[sequence] == str():
            bit_word[sequence] = 1


def init_word_list():
    global bit_word
    global plain_word
    
    bit_word = [plain_word[0]]
    for a in range(len(plain_word)):
        if a > 1:
            if plain_word[a] == plain_word[0]:
                bit_word.append(plain_word[a])
                
        if plain_word[a] != plain_word[0]:
            bit_word.append(int(0))

def feedback_to_user():
    global bit_word
    global user_offer
    
    guess = False
    
    for sequence in range(len(bit_word)):
        
        if user_offer == bit_word[sequence]:
            
            guess = True
                    
    if guess == True:
        
        print("\nYou have guessed a letter!")
        
    if guess == False:
        
        print("\nTry again!")
        
        
game_state = 0

while True:    
    # Introduction and explanation for a player
    if game_state == 0:
        
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
              "In total you have 3 lives."
              "\n\n"
              "------------------------------------------------------")
        game_state = 1
    
    # Initializing first variables and choosing a random word
    if game_state == 1:
        
        lives = 3
        
        plain_word = choice(plain_words_list)
        init_word_list()
        print("\nYour first word starts with letter {}.\n".format(plain_word[0]))
        bit_to_word()
        
        game_state = 2
        
    if game_state == 2:
        
        user_offer = input("\nPlease enter your guess: ")
        
        if user_offer == bit_word[0]:
            
            print("\nThis letter is already exists!")
            user_offer = input("Please enter letter again: ")
            
        if user_offer.isdigit():
            
            print("\nYou have entered a number!")
            user_offer = input("Please enter a letter: ")
            
        user_offer = user_offer.lower()
        
        word_to_bit()
        bit_check()
        bit_to_word()
        feedback_to_user()
        word_to_bit()
