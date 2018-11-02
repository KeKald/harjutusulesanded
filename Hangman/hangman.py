from random import choice

with open("C:\\Users\\kekalda\\Documents\\Proge\\harjutusulesanded\\Hangman\\words.txt", "r", encoding = "utf-8") as text:
    words_list = []
    for line in text:
        words_list.append(line.replace("\n", ""))

print(words_list)

word = choice(words_list)
print(word)

underline = "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "
print(word[0:1], underline[0:len(word)])