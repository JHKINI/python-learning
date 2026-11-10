from collections import deque

maze = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '0', '1'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '0', '1', '0', '0', 'x'],
    ['1', '1', '1', '1', '1', '1']
]

MAZE_SIZE = 6

def is_valid_pos(r, c):
    if r < 0 or c < 0 or r >= MAZE_SIZE or c >= MAZE_SIZE:
        return False
    return maze[r][c] == '0' or maze[r][c] == 'x'


def bfs():
    queue = deque()
    queue.append((1, 0))  # 시작 위치

    while queue:
        r, c = queue.popleft()
        print("현재 위치:", (r, c))

        if maze[r][c] == 'x':
            print("출구 발견!")
            return True

        maze[r][c] = '.'  # 방문 표시

        # 앞 → 좌 → 우 → 뒤 순서 
        if is_valid_pos(r - 1, c):  # 앞
            queue.append((r - 1, c))

        if is_valid_pos(r, c - 1):  # 좌
            queue.append((r, c - 1))

        if is_valid_pos(r, c + 1):  # 우
            queue.append((r, c + 1))

        if is_valid_pos(r + 1, c):  # 뒤
            queue.append((r + 1, c))

    print("출구 못 찾음")
    return False


bfs()