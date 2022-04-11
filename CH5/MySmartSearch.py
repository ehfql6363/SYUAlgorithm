from CH5.PriorityQueue import PriorityQueue
import math
(oRow, oCol) = (4,5)
def dist(row, col):
    nRow, nCol = row - oRow, col - oCol
    return math.sqrt(nRow*nRow + nCol*nCol)

def mySmartSearch():
    q = PriorityQueue()
