from CH4.Stack import Stack

map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '0', 'x'],
       ['1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '1']]

MAZE_MAX = 6


def isValidPos(row, col):
    if row < 0 or row >= MAZE_MAX or col < 0 or col >= MAZE_MAX:
        return False
    else:
        return map[row][col] == '0' or map[row][col] == 'x'


def dfs():
    s = Stack()

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'e':
                s.push((i, j))
                break

    print("DFS : (row, col)")

    while not s.isEmpty():
        here = s.pop()

        print(here, end='->')
        (row, col) = here

        if map[row][col] == 'x':
            return True
        else:
            map[row][col] = '.'  # 방문한 곳 체크
            if isValidPos(row - 1, col): s.push((row - 1, col))
            if isValidPos(row, col - 1): s.push((row, col - 1))
            if isValidPos(row + 1, col): s.push((row + 1, col))
            if isValidPos(row, col + 1): s.push((row, col + 1))

        print('현재 스택: ', s.top)

    return False  # 다 돌아도 안나온다면 False


if dfs():
    print("탈출")
else:
    print("ㅠㅠ")
