'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

answer = 20
# Only need to check using numbers between 11 and 20 because everything below that is a factor of one of these numbers
numList = (11,12,13,14,15,16,17,18,19,20)
while(True):
    for i in numList:
        if answer % i != 0:
            break
    else:
        break
    answer += 20
print answer
