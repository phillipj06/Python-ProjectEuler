# Compact version
print  sum([number for number in xrange(1000) if not number %3  or not number % 5 ])

# Expanded version
sum = 0
for num in xrange(1000):
    if num % 3 == 0 or num % 5 == 0:
       sum += num 
print sum
