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

    for i in range(len(map)): # 시작지점찾기
        for j in range(len(map[i])):
            if map[i][j] == 'e':
                q.enqueue((i, j))#찾았으면 큐에 row, col형태로 넣기

    print("BFS : (row, col)")
    print(f"시작지점 = {q.peek()}")

    while not q.isEmpty(): #큐가 빌 때까지
        here = q.dequeue() #현재 위치는 큐의 값 하나 뺴온 것
        print(here, end='->') #현재 위치 출력
        (row, col) = here #현재 위치의 row값과 col값을 변수 지정
        if map[row][col] == 'x': #map상에서 row, col이 도착지점이면
            return True #바로 True 반환
        else: #도착 지점이 아닌 다른 곳이라면
            map[row][col] = '.' #현재 위치를 이미 왔던 곳으로 표시 ex) .으로 표시함
            if isValidPosition(row - 1, col): q.enqueue((row - 1, col)) #상하좌우로 탐색하고
            if isValidPosition(row, col - 1): q.enqueue((row, col - 1)) #탐색이 가능하면 해당 값을
            if isValidPosition(row + 1, col): q.enqueue((row + 1, col)) #(nRow, nCol)형태로 큐에 삽입
            if isValidPosition(row, col + 1): q.enqueue((row, col + 1))

    return False #while 문 끝까지 돌렸는데도 안나오면 False반환

#test
# if bfs():
#     print("탈출")
# else:
#     print("ㅠㅠ")
