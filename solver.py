"""Write a function that returns the largest palindrome from the product of two n-digit numbers """

def solver(n, p=None, q=None):
    """function that returns the largest palindrome from the product of two n-digit numbers """
    if p is None:
        p = 10 ** (n - 1)
    if q is None:
        q = 10**n - 1

    largest_palindrome = 0
    for i in range(q, p, -1):
        for j in range(i, p, -1):
            product = i * j
            if product >= largest_palindrome:
                break
            if str(product) == str(product)[::-1]:
                largest_palindrome = product
                break
    return largest_palindrome


if __name__ == "__main__":
    print(solver(4))
