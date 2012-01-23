from utils import timeIt
@timeIt
def problem48():
    print str(sum(i**i for i in range(1,1001)))[-10:]
problem48()
