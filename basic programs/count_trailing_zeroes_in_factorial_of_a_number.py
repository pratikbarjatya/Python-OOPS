# Given an integer n, write a function that returns count of trailing zeroes in n!.
"""
Examples :

Input: n = 5
Output: 1
Factorial of 5 is 120 which has one trailing 0.

Input: n = 20
Output: 4
Factorial of 20 is 2432902008176640000 which has 4 trailing zeroes.

Input: n = 100
Output: 24

Trailing 0s in n! = Count of 5s in prime factors of n!
                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
"""


# Function to return trailing 0s in factorial of n
def find_trailing_zeros(num):
    # Initialize result
    count = 0

    # Keep dividing n by powers of 5 and update Count
    i = 5
    while num / i >= 1:
        count += int(num / i)
        i *= 5
    return int(count)


# Driver program
n = 100
print("Count of trailing 0s in 100 ! is", find_trailing_zeros(n))
