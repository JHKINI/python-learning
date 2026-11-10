from queue import PriorityQueue

#현재위치에서 갈수있곳들을 큐에 집어넣고 칸이 
# 출구와 거리가 얼마나 되는지 고려하여 가까운것부터꺼내온다 
# (d는 멀수록 큰값 작을수록 가까운 값 그래서 출구로 부터 가까운곳을 찾기 위해 -d를 고려 )



maze = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '0', '1'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '0', '1', '0', '0', 'x'],
    ['1', '1', '1', '1', '1', '1']
]

MAZE_SIZE = 6
exit_pos = (4, 5)

def distance(r, c):
    er, ec = exit_pos
    return abs(er - r) + abs(ec - c)

def is_valid_pos(r, c):
    if r < 0 or c < 0 or r >= MAZE_SIZE or c >= MAZE_SIZE:
        return False
    return maze[r][c] == '0' or maze[r][c] == 'x'

def priority_maze_search():
    q = PriorityQueue()

    # (거리, 위치)
    q.put((distance(1, 0), (1, 0)))

    while not q.empty():
        d, here = q.get()
        r, c = here

        print("현재 위치:", here, "출구까지 거리:", d)

        if maze[r][c] == 'x':
            print("출구 발견!")
            return True

        maze[r][c] = '.'

        # 상하좌우 탐색
        if is_valid_pos(r - 1, c):
            q.put((distance(r - 1, c), (r - 1, c)))

        if is_valid_pos(r + 1, c):
            q.put((distance(r + 1, c), (r + 1, c)))

        if is_valid_pos(r, c - 1):
            q.put((distance(r, c - 1), (r, c - 1)))

        if is_valid_pos(r, c + 1):
            q.put((distance(r, c + 1), (r, c + 1)))

    print("출구를 찾을 수 없음")
    return False

priority_maze_search()