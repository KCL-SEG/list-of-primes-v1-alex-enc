"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    for x in range(2,number_of_primes + 2):
        prime = True
        for y in range(2,x):
            if (x%y==0):
                prime = False
        if prime:
            list.append(x)

    return list
