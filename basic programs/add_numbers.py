# Python3 program to add two numbers
number1 = input("First number: ")
number2 = input("\nSecond number: ")
# Adding two numbers
# User might also enter float numbers
addition = float(number1) + float(number2)
# Display the sum
# will print value in float
print("The sum of {0} and {1} is {2}".format(number1, number2, addition))

# Python program to add two hexadecimal numbers.
# Declaring the variables
a = "123"
b = "456"
# Calculating octal value using function
octal_sum = oct(int(a, 8) + int(b, 8))
# Printing result
print(octal_sum[2:])

# Python program to add two hexadecimal numbers.
# Declaring the variables
a = "01B"
b = "378"
# Calculating hexadecimal value using function
hex_sum = hex(int(a, 16) + int(b, 16))
# Printing result
print(hex_sum[2:])

# Python program to add two binary numbers.
# Declaring the variables
a = "1101"
b = "100"
max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)
# Initialize the result
result = ''
# Initialize the carry
carry = 0
# Traverse the string
for i in range(max_len - 1, -1, -1):
    r = carry
    r += 1 if a[i] == '1' else 0
    r += 1 if b[i] == '1' else 0
    result = ('1' if r % 2 == 1 else '0') + result
    # Compute the carry.
    carry = 0 if r < 2 else 1
if carry != 0:
    result = '1' + result
print(result.zfill(max_len))

# Python program to add two binary numbers.
# Declaring the variables
a = "1101"
b = "100"
# Calculating binary value using function
bin_sum = bin(int(a, 2) + int(b, 2))
# Printing result
print(bin_sum[2:])

# Program to add two matrices using nested loop
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)

# using list comprehension
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
result = [[X[i][j] + Y[i][j] for j in range (len(X[0]))] for i in range(len(X))]
for r in result:
    print(r)

# using zip()
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
result = [map(sum, zip(*t)) for t in zip(X, Y)]
print(result)
