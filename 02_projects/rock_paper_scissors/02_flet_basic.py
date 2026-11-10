import flet as ft
import random

def main(page: ft.Page):
    result_text = ft.Text("결과가 여기에 표시됩니다")

    def play(e):
        user = e.control.text  # 버튼에 적힌 값
        computer = random.choice(["가위", "바위", "보"])

        if user == computer:
            result = "비김"
        elif (user == "가위" and computer == "보") or \
             (user == "바위" and computer == "가위") or \
             (user == "보" and computer == "바위"):
            result = "이김"
        else:
            result = "짐"

        result_text.value = f"나: {user}, 컴퓨터: {computer} → {result}"
        page.update()

    page.add(
        ft.Row([
            ft.ElevatedButton("가위", on_click=play),
            ft.ElevatedButton("바위", on_click=play),
            ft.ElevatedButton("보", on_click=play),
        ]),
        result_text
    )

# ft.run(main, view = ft.AppView.WEB_BROWSER)
ft.app(target = main)