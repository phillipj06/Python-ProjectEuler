from utils import isPrime, timeIt
@timeIt
def problem10():
    print sum([x for x in xrange(2000000) if isPrime(x)])
problem10()

