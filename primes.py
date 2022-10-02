

"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    freq= {}
    amountOfPrimes = 1

    x = 2
    if number_of_primes == 0:
        list = []
    else:

        list.append(2)
        while amountOfPrimes < number_of_primes:
            x += 1
            prime = True


            for y in range(2,x):
                if (x%y==0):
                    prime = False
            if prime:
                if x in freq:
                    freq[x] +=1
                else:
                    amountOfPrimes += 1
                    list.append(x)
                    freq[x] = 1

    return list
