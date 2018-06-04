#String Challenges

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