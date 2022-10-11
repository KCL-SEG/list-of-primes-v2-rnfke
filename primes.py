"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError

    list = []
    x = 2
    while len(list) < number_of_primes:
        flag = False
        for i in range (2,x):
            if i!=x:
                if x%i==0:
                    flag = True
            else:
                pass
        if flag==False:
            list.append(x)

        x = x + 1
    return list
