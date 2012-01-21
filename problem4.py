'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def palFinder(maxNum,minNum):
    answer =0
    for i in range(maxNum,minNum-1,-1):
        for j in range(i,minNum-1,-1):
            product=i*j
            if answer < product:
                if (palCheck(product)):
                    answer =  product
    return answer
def palCheck(num):
    stringNum = str(num)
    halfPoint=len(stringNum)/2
    return stringNum[:halfPoint]==stringNum[-halfPoint:][::-1]

def testLogic():
    if palFinder(99,10) != 9009:
        print 'Logic is bad. 9009 != ' + str(palFinder(99,10))
        import sys
        sys.exit(-1)
    else:
        print 'Logic is good'

#testLogic()
print palFinder(999,100)
