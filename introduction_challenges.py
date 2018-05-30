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