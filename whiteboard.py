# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# deleted - or _
# letter after the - or _ converted to capital


def solution(string):
    upper_word = False
    new_string = ''
    for letter in string:
        if letter == '_' or letter == '-' or letter == ' ':
            upper_word = True
        else: 
            if upper_word == True:
                letter = letter.upper()
                upper_word = False
            new_string += letter
    return new_string