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


def dfs():
    from Stack import Stack
    maze = Stack()
    maze.push((1, 0))

    while not maze.isEmpty():
        here = maze.pop()
        print(here, end='->')
        (row, col) = here

        if map[row][col] == 'x':
            return True
        else:
            map[row][col] = '.'

            if isValidPosition(row - 1, col):
                maze.push((row - 1, col))
            if isValidPosition(row, col - 1):
                maze.push((row, col - 1))
            if isValidPosition(row + 1, col):
                maze.push((row + 1, col))
            if isValidPosition(row, col + 1):
                maze.push((row, col + 1))

        print("이동:", maze.peek())

    return False


if dfs():
    print("탈출 가능!")
else:
    print("탈출 불가능ㅠ")
