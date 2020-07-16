def pyramid_pattern(n):
    """
    Pyramid Pattern Program
    :param n:
    :return:
    """
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")


def reverse_pyramid_pattern(n):
    """
    Reverse Pyramid Pattern Program
    :param n:
    :return:
    """
    k = 2 * n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")


def right_start_pattern(n):
    """
    Right Start Pattern Program
    :param n:
    :return:
    """
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    for i in range(n, 0, -1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


def left_start_pattern(n):
    """
    Left Start Pattern Program
    :param n:
    :return:
    """
    k = 2 * n - 2
    for i in range(0, n-1):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = -1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


def hourglass_pattern(n):
    """
    Hourglass Pattern Program
    :param n:
    :return:
    """
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = 2 * n - 2
    for i in range(0, n + 1):
        for j in range(0, k):
            print(end="")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


def half_pyramid_pattern(n):
    """
    Half-Pyramid Pattern Program
    :param n:
    :return:
    """
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


def left_half_pyramid_pattern(n):
    """
    Left Half-Pyramid Pattern Program
    :param n:
    :return:
    """
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


def downward_half_pyramid_pattern(n):
    """
    Downward Half-Pyramid Pattern Program
    :param n:
    :return:
    """
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


def diamond_pattern(n):
    """
    Diamond Shaped Pattern Program
    :param n:
    :return:
    """
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


def diamond_star_pattern():
    for i in range(5):
        for j in range(5):
            if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
                print("*", end="")
            else:
                print(end=" ")
        print()


def simple_numbers_pattern(n):
    """
    Simple Numbers Program
    :param n:
    :return:
    """
    x = 0
    for i in range(0, n):
        x += 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")


def pascal(n):
    """
    Pascal’s Triangle Program
    :param n:
    :return:
    """
    for i in range(0, n):
        for j in range(0, i + 1):
            print(function(i, j), " ", end="")
        print()


def function(n, k):
    """

    :param n:
    :param k:
    :return:
    """
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    return res


def half_pyramid_with_numbers_pattern(n):
    """
    Half-Pyramid Pattern With Numbers
    :param n:
    :return:
    """
    for i in range(1, n):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("\r")


def diamond_with_numbers_pattern(n):
    """
    Diamond Pattern With Numbers
    :param n:
    :return:
    """
    k = 2 * n - 2
    x = 0
    for i in range(0, n):
        x += 1
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")
    k = n - 2
    x = n + 2
    for i in range(n, -1, -1):
        x -= 1
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")


def descending_order_pattern(n):
    """
    Descending Order Pattern Program
    :param n:
    :return:
    """
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")

        print("\r")


def binary_numbers_pattern(n):
    """
    Binary Numbers Pattern Program
    :param n:
    :return:
    """
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print('10', end="")

        print("\r")


def right_alphabetical_triangle_pattern(n):
    """
    Right Alphabetical Triangle
    :param n:
    :return:
    """
    x = 65
    for i in range(0, n):
        ch = chr(x)
        x += 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("\r")


def character_pattern(n):
    """
    Character Pattern Program
    :param n:
    :return:
    """
    k = 2 * n - 2
    x = 65
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            ch = chr(x)
            print(ch, end=" ")
            x += 1
        print("\r")


def k_shape_character_pattern():
    """
    K Shape Character Program
    :return:
    """
    for i in range(7):
        for j in range(7):
            if j == 0 or i - j == 3 or i + j == 3:
                print("*", end="")
            else:
                print(end=" ")
        print()


def triangle_character_pattern(n):
    """
    Triangle Character Pattern Program
    :param n:
    :return:
    """
    k = 2 * n - 2
    x = 65
    for i in range(0, n):
        ch = chr(x)
        x += 1
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("\r")


def diamond_shaped_character_pattern(n):
    """
    Diamond Shaped Character Pattern Program
    :param n:
    :return:
    """
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        x = 65
        for j in range(0, i + 1):
            ch = chr(x)
            print(ch, end=" ")
            x += 1
        print("\r")
    k = n - 2
    x = 65
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            ch = chr(x)
            print(ch, end=" ")
            x += 1
        print("\r")


pyramid_pattern(5)
print("\n")
reverse_pyramid_pattern(5)
print("\n")
right_start_pattern(5)
print("\n")
left_start_pattern(5)
print("\n")
hourglass_pattern(5)
print("\n")
half_pyramid_pattern(5)
print("\n")
left_half_pyramid_pattern(5)
print("\n")
downward_half_pyramid_pattern(5)
print("\n")
diamond_pattern(5)
print("\n")
diamond_star_pattern()
print("\n")
simple_numbers_pattern(5)
print("\n")
pascal(7)
print("\n")
half_pyramid_with_numbers_pattern(5)
print("\n")
diamond_with_numbers_pattern(5)
print("\n")
descending_order_pattern(5)
print("\n")
binary_numbers_pattern(5)
print("\n")
right_alphabetical_triangle_pattern(5)
print("\n")
character_pattern(7)
print("\n")
k_shape_character_pattern()
print("\n")
triangle_character_pattern(5)
print("\n")
diamond_shaped_character_pattern(5)
print("\n")
