def string_check(string):
    no_digits = []

    if string.isdigit() == True:
        for a in string:
            if not string.isdigit():
                no_digits.append(a)
        return "".join(no_digits)

    if string.isdigit() == False:
        return string

name = str(input("Please enter you name: \n"))
adjective = str(input("Please enter a adjective: \n"))
noun = str(input("Please enter a noun: \n"))
verb = str(input("Please enter a verb: \n"))

string_check(name)
string_check(adjective)
string_check(noun)
string_check(verb)

print("Mina {0} olen {1} {2} ja ma {3}".format(name.capitalize(), adjective.lower(), noun.lower(), verb.lower()))