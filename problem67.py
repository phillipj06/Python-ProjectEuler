from utils import timeIt
'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
'''
@timeIt
def problem67():
    data = open("problem67.data").readlines()
    triangleData = [[int(num) for num in line.split()] for line in data]
    length = len(triangleData)

    '''
    This algorithm goes through each row from the bottom up.  
    For each number encountered it sees if it or its adjacent numbers are 
    larger then adds that to the neighbor number in the next row up
    This continues until the top is reached, and the only value left
    is the maximum sum path

    To see this clearly uncomment the print statement
    '''
    for row in xrange(length-2,-1,-1):
        for col in xrange(row+1):
            triangleData[row][col] += max(triangleData[row+1][col], triangleData[row+1][col+1])
        #print  triangleData[row]
    print triangleData[0][0]

problem67()
