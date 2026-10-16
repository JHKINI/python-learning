# 미로 탐색 - 스택을 이용한 깊이 우선 탐색 DFS



map=[

    ['1', '1', '1', '1', '1', '1'],

    ['e', '0', '1', '0', '0', '1'],

    ['1', '0', '0', '0', '1', '1'],

    ['1', '0', '1', '0', '1', '1'],

    ['1', '0', '1', '0', '0', 'x'],

    ['1', '1', '1', '1', '1', '1']

]



MAP_SIZE = 6



stack = []



def is_valid_pos(x, y):

    if x < 0 or y < 0 or x >= MAP_SIZE or y >= MAP_SIZE:

        return False



    if map[x][y] == '0' or map[x][y] == 'x':

        return True

    else:

        return False





def dfs():

    stack.append((1, 0))   # 시작 위치 e



    while len(stack) != 0:

        here = stack.pop()

        x = here[0]

        y = here[1]



        print("현재 위치:", here)



        if map[x][y] == 'x':

            print("출구 발견!")

            return True



        map[x][y] = '.'   # 방문 표시



        # 갈 수 있는 곳 확인

        # 스택은 나중에 넣은 것이 먼저 나옴

         

        # 뒤

        if is_valid_pos(x + 1, y):

            stack.append((x + 1, y))



        # 오른쪽

        if is_valid_pos(x, y + 1):

            stack.append((x, y + 1))



        # 왼쪽

        if is_valid_pos(x, y - 1):

            stack.append((x, y - 1))



        # 앞

        if is_valid_pos(x - 1, y):

            stack.append((x - 1, y))



    print("출구를 찾을 수 없음")

    return False





dfs()