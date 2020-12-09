# Find the last digit when factorial of A divides factorial of B
"""We are given two numbers A and B such that B >= A. We need to compute the last digit of this resulting F such that
F = B!/A! where 1 = A, B <= 10^18 (A and B are very large).

Examples:

Input : A = 2, B = 4
Output : 2
Explanation : A! = 2 and B! = 24.
F = 24/2 = 12 --> last digit = 2

Input : 107 109
Output : 2

Approach
Factorial function grows on an exponential rate. Even the largest data type
cannot hold factorial of numbers like 100

Here the given constraints are very large. Thus, calculating the two factorials and later
dividing them and computing the last digit is practically an impossible task.

Thus we have to find an alternate approach to break down our problem.
It is known that the last digit of factorial always belongs to the set {0, 1, 2, 4, 6}
The approach is as follows: –
1) We evaluate the difference between B and A
2) If the (B – A) >= 5, then the answer is always 0
3) If the difference (B – A) < 5, then we iterate from (A+1) to B, multiply and store them.
multiplication_answer % 10 shall be our answer.
"""


# Function which computes the last digit of resultant of B!/A!
def compute_last_digit(a, b):
    variable = 1
    if a == b:  # If a = b, b! = a! and b!/a! = 1
        return 1
    # If difference (b - a) >= 5, answer = 0
    elif (b - a) >= 5:
        return 0
    else:
        # If non of the conditions  are true, we iterate from  A+1 to B and multiply them.
        # We are only concerned for the last digit, thus we take modulus of 10
        for i in range(a + 1, b + 1):
            variable = (variable * (i % 10)) % 10
        return variable % 10


# driver function
print(compute_last_digit(2632, 2634))
