"""Find the largest palindrome """


def answer():
    """function for finding largest palindrome"""
    largest_palindrome = 0
    for i in range(999, 101, -1):
        for j in range(i, 101, -1):
            product = i * j
            if product <= largest_palindrome:
                break
            if str(product) == str(product)[::-1]:
                largest_palindrome = product
                break
    return largest_palindrome


if __name__ == "__main__":
    print(answer())
