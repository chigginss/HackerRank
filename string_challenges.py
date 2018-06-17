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

"""Read a given string, change the character at a given index and then print the modified string."""

def mutate_string(string, position, character):
    
    l = list(string)
    l[position] = character
    str = "".join(l)
    return str

"""Text Alignment
You are given a partial code that is used for generating the HackerRank Logo of variable thickness. """

thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)    

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)

""" You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
 """

# Not complete - needs revision
def solve(s):
    str = s.split(" ")
    new_s = []
    
    if str[0][0].isalpha():
        new_s = str[0][0].upper() + str[0][1:].lower()
    
    if str[1][0].isalpha():
        new_s = new_s + " " + str[1][0].upper() + str[1][1:].lower()
    
    result = "".join(new_s)
    
    # result = str(result)
    
    print result



