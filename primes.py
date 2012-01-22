def isPrime(num):
    '''
    isPrime checks to see if the number passed to it is a prime number.
    '''
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    i = 3
    while i <= int(num ** 0.5):
        if num % i == 0:
            return False
        i += 2
    return True
