from primes import isPrime
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
def maxPrimeFactor(number):
    '''
    maxPrimeFactor takes a number and returns the largest prime factor for that number
    '''
    # The largest factor of a number cannot be larger then the square root of the number
    maxFactor = int(number ** 0.5)
    while maxFactor > 1:
        if number % maxFactor == 0:
            if isPrime(maxFactor):
                return maxFactor
        maxFactor -= 1
    # If the while loop did not return a value then the orginal number has to be prime
    return number

def testLogic():
    '''
    A quick test to check the logic for the problem
    '''
    answer =  maxPrimeFactor(13195) 
    if answer != 29: 
        print 'Logic is bad. Answer = 29.  Result =' +str(answer)
    else:
        print 'Logic is good'

testLogic()
print maxPrimeFactor(600851475143)
