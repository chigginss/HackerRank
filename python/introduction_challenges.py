""" First Python Problems from HackerRank"""


""" 
If-Else 

Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer, n."""

def is_weird(n):
    if n % 2 == 1:
        print "Weird"
    elif n % 2 == 0 and 2 <= n <= 5:
        print "Not Weird"
    elif n % 2 == 0 and 6 <= n <= 20:
        print "Weird"
    elif n % 2 == 0 and n > 20:
        print "Not Weird"

if __name__ == '__main__':
    n = int(raw_input())
    is_weird(n)


""" 
Arithmetic Operators
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Input Format

The first line contains the first integer, . The second line contains the second integer, .

Constraints

 1 < a < 10^10
 1 < b < 10^10

Output Format

Print the three lines as explained above."""

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print (a + b)
    print (a - b)
    print (a * b)

""" 
Division 
Read two integers and print two lines. The first line should contain integer division,  a//b . The second line should contain float division,  a/b .

You don't need to perform any rounding or formatting operations.

Input Format

The first line contains the first integer, a . The second line contains the second integer, b.

Output Format

Print the two lines as described above."""

from __future__ import division

def division(a, b):
    print int(round(a / b))
    print a / b

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    division(a,b)

""""
Loops
Read an integer N. For all non-negative integers i < N , print i^2. See the sample for details.

Input Format

The first and only line contains the integer, N.

Constraints

i < N < 20

Output Format

Print N lines, one corresponding to each i. """

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        print i**2

""" 
Write a function

We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February. 
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source

Task 
You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.

Input Format

Read y, the year that needs to be checked.

Constraints

1900 < y < 10^5

Output Format

Output is taken care of by the template. Your function must return a boolean value (True/False) """

def is_leap(year):
    
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 400 == 0 and year % 100 == 0:
        leap = True
    else:
        leap = False

    return leap

""" 

Print function 

Read an integer N.

Without using any string methods, try to print the following:

123..N

Note that "..." represents the values in between.

Input Format

The first line contains an integer N.

Output Format

Output the answer as explained in the task."""

from __future__ import print_function
print(*range(1, input() + 1), sep="")
    
if __name__ == '__main__':
    n = int(raw_input())
    
""" Make anagrams """

def number_needed(a, b):
    H = {}
    count = 0
    for i in range(len(a)):
        if not H.get(a[i]):
            H[a[i]] = 1
        else:
            H[a[i]] += 1

    for i in range(len(b)):
        if H.get(b[i]):
            H[b[i]] -= 1
        else:
            count += 1
    for v in H.values():
        count += v
    return count

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)





