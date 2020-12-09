# Python 3 program to find
# factorial of given number
def factorial_f1(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial_f1(n - 1)


# factorial of given number
def factorial_f2(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact


# Recursion
def factorial_f3(n):
    # Checking the number
    # is 1 or 0 then
    # return 1
    # other wise return
    # factorial
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_f3(n - 1)


num = 5
print("Factorial of", num, "is", factorial_f1(num))
print("Factorial of", num, "is", factorial_f2(num))
