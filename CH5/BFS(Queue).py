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


def bfs():
    q = CircularQueue()

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'e':
                q.enqueue((i, j))

    print("BFS : (row, col)")
    print(f"시작지점 = {q.peek()}")

    while not q.isEmpty():
        here = q.dequeue()
        print(here, end='->')
        (row, col) = here
        if map[row][col] == 'x':
            return True
        else:
            map[row][col] = '.'
            if isValidPosition(row - 1, col): q.enqueue((row - 1, col))
            if isValidPosition(row, col - 1): q.enqueue((row, col - 1))
            if isValidPosition(row + 1, col): q.enqueue((row + 1, col))
            if isValidPosition(row, col + 1): q.enqueue((row, col + 1))

    return False


if bfs():
    print("탈출")
else:
    print("ㅠㅠ")
