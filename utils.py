def timeIt(f):
    ''' 
    Decorator to be used to time problem runs in to determine performance
    '''
    def new_f():
        import time     
        start = time.time()     
        answer = f()                    
        print 'Runtime for ' + f.__name__ + ' = ' + str(time.time() - start) 
        return answer

    return new_f   
    
def sumDigits(num): 
    return sum([int(i) for i in str(num)])

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

