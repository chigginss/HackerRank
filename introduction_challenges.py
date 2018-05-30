""" First Python Problems """


""" 
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