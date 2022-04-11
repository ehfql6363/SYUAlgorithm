from CH5.Queue import CircularQueue

map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '0', 'x'],
       ['1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '1']]

MAZE_MAX = 6

def isValidPosition(row, col):
    if row < 0 or col < 0 or row > MAZE_MAX or col > MAZE_MAX:
        return False
    else:
        return map[row][col] == '0' or map[row][col] == 'x'

def BFS():
    que = CircularQueue()
    que.enqueue((1,0))
    print("BFS :")

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')

        row, col = here
        if(map[row][col] == 'x'):
            return True
        else:
            map[row][col] = '.'
            if isValidPosition(row-1, col):
                que.enqueue((row-1, col))
            if isValidPosition(row, col-1):
                que.enqueue((row, col-1))
            if isValidPosition(row+1, col):
                que.enqueue((row + 1, col))
            if isValidPosition(row, col+1):
                que.enqueue((row, col+1))