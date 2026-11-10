# -*- coding: utf-8 -*-
# 미로 탐색 DFS - Flet 버전

import flet as ft


maze = [
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

    if maze[x][y] == '0' or maze[x][y] == 'x':
        return True
    else:
        return False


def main(page: ft.Page):
    page.title = "DFS 미로 탐색"
    page.window.width = 500
    page.window.height = 600

    result_text = ft.Text("DFS 미로 탐색 시작 전", size=18)
    log = ft.Column(scroll=ft.ScrollMode.AUTO, height=250)

    maze_view = ft.Column()

    def draw_maze():
        maze_view.controls.clear()

        for i in range(MAP_SIZE):
            row = ft.Row()

            for j in range(MAP_SIZE):
                cell = maze[i][j]

                if cell == '1':
                    color = ft.Colors.BLACK
                    text = "벽"
                elif cell == '0':
                    color = ft.Colors.WHITE
                    text = ""
                elif cell == 'e':
                    color = ft.Colors.GREEN
                    text = "입구"
                elif cell == 'x':
                    color = ft.Colors.RED
                    text = "출구"
                elif cell == '.':
                    color = ft.Colors.BLUE
                    text = "지나온길"

                row.controls.append(
                    ft.Container(
                    content=ft.Text(text),
                    width=60,
                    height=60,
                    border=ft.border.all(1)
                )
        )

            maze_view.controls.append(row)

        page.update()

    def dfs_click(e):
        stack.clear()
        stack.append((1, 0))

        while len(stack) != 0:
            here = stack.pop()
            x = here[0]
            y = here[1]

            log.controls.append(ft.Text(f"현재 위치: {here}"))

            if maze[x][y] == 'x':
                result_text.value = "출구 발견!"
                draw_maze()
                page.update()
                return

            if maze[x][y] != 'e':
                maze[x][y] = '.'

            if is_valid_pos(x + 1, y):
                stack.append((x + 1, y))

            if is_valid_pos(x, y + 1):
                stack.append((x, y + 1))

            if is_valid_pos(x, y - 1):
                stack.append((x, y - 1))

            if is_valid_pos(x - 1, y):
                stack.append((x - 1, y))

        result_text.value = "출구를 찾을 수 없음"
        page.update()

    start_button = ft.ElevatedButton("DFS 실행", on_click=dfs_click)

    page.add(
        ft.Text("스택을 이용한 깊이 우선 탐색 DFS", size=22),
        maze_view,
        start_button,
        result_text,
        ft.Text("탐색 과정"),
        log
    )

    draw_maze()


ft.app(target=main)