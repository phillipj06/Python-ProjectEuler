'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''


'''
a**2 + b**2 = c**2
c = (a**2+b**2)**0.5

a+b+c=1000
c=1000-(a+b)

1000-(a+b)=(a**2+b**2)**0.5
1000 = (a**2+b**2)**0.5+(a+b)
'''

def findAnswer():
    for a in range(1,1001):
	for b in xrange(1,1001):
	    if 1000== (a**2 + b**2)**0.5 + (a+b): 
		c = 1000-(a+b)	
		return a*b*c

print findAnswer()
