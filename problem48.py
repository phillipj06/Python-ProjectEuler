from timeIt import timeIt
@timeIt
def getAnswer():
    print str(sum(i**i for i in range(1,1001)))[-10:]
getAnswer()
