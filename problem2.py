a=1
b=2
# the answer needs to contain the starting values of 2
answer = 2
while b < 4000000:
    a,b=b,a+b
    if not b % 2:
        answer += b
print answer

