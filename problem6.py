'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
# One line version
print sum(xrange(101))**2 - sum((i**2 for i in xrange(101)))

# Extended version
def prob6(top):
    #Need to add 1 to ajust for the range function
    top+=1
    sumSquare = sum((i**2 for i in xrange(top)))
    squareSum = sum(xrange(top))**2
    return (squareSum - sumSquare)

def testLogic():
    '''
    A quick test to check the logic for the problem
    '''
    answer =  prob6(10)
    if answer != 2640:
        print 'Logic is bad. Answer = 2640.  Result =' +str(answer)
    else:
        print 'Logic is good'
#testLogic()
#prob6(100)

