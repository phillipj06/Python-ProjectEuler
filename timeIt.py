def timeIt(f):
    '''
    Decorator to be used to time problem runs in to determine performance
    '''
    def new_f():
        import time
        start = time.time()
        answer = f()
        print 'Runtime = ' + str(time.time() - start)
        return answer
    return new_f

