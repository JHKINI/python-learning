import random
import flet as ft

def main(page: ft.Page):
    page.title = "가위바위보 게임"
    page.bgcolor = ft.colors.LIGHT_YELLOW  # 배경 연한 노랑

    choices = ["가위", "바위", "보"]
    player = 0
    computer = 0

    result = ft.Text("가위 바위 보 중에서 선택해 주세요")
    score = ft.Text("나: 0 | 컴퓨터: 0")

    # 버튼 스타일
    button_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=8),
        side=ft.BorderSide(2, ft.colors.PINK)
    )

    def game(user):
        nonlocal player, computer

        com = random.choice(choices)

        if user == com:
            result.value = "무승부"
        else:
            if (user == "가위" and com == "보") or \
               (user == "바위" and com == "가위") or \
               (user == "보" and com == "바위"):
                player += 1
                result.value = "이김"
            else:
                computer += 1
                result.value = "짐"

        score.value = f"나: {player} | 컴퓨터: {computer}"

        if player == 3:
            result.value = "최종 승리!"
        elif computer == 3:
            result.value = "컴퓨터 승리!"

        page.update()

    # UI 구성
    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.ElevatedButton("가위", on_click=lambda e: game("가위"), style=button_style),
                        ft.ElevatedButton("바위", on_click=lambda e: game("바위"), style=button_style),
                        ft.ElevatedButton("보", on_click=lambda e: game("보"), style=button_style),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Container(result, alignment=ft.alignment.center, margin=10),
                ft.Container(score, alignment=ft.alignment.center, margin=10)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)