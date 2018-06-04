"""String Challenges"""

"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

def swap_case(s):
    
    new_string = ""
    
    for letter in s:
        if letter == letter.upper():
            letter = letter.lower()
        elif letter == letter.lower():
            letter = letter.upper()
        new_string += letter
    
    return new_string

"""You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python."""

def print_full_name(a, b):
    print "Hello {} {}! You just delved into python.".format(a, b)

""" You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen. """

def split_and_join(line):
    new_line = line.split(" ")
    return "-".join(new_line)



