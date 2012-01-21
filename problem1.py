'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
# Compact version
print  sum([number for number in xrange(1000) if not number %3  or not number % 5 ])

# Expanded version
sum = 0
for num in xrange(1000):
    if num % 3 == 0 or num % 5 == 0:
       sum += num 
print sum
