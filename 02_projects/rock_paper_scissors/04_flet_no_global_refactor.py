import random
import flet as ft

def main(page: ft.Page):
    # 1. 게임 상태 변수 (함수 안에 두면 전역 변수를 줄일 수 있어요)
    page.title = "가위바위보 게임 (3판 선승제)"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    status = {"player": 0, "computer": 0} # 점수를 딕셔너리로 관리
    choices = ["가위", "바위", "보"]

    # 2. 화면 구성 요소 정의
    result_text = ft.Text("버튼을 눌러 게임을 시작하세요!", size=20)
    score_text = ft.Text("현재 스코어 - 나: 0 | 컴퓨터: 0", size=16, color="blue")
    
    # 리셋 버튼 (처음엔 숨김)
    reset_button = ft.ElevatedButton(
        "다시 시작하기", 
        visible=False, 
        on_click=lambda _: restart_game()
    )

    # 3. 게임 로직 함수
    def play(player_pick):
        if status["player"] >= 3 or status["computer"] >= 3:
            return

        com_pick = random.choice(choices)
        
        # 승패 로직
        if player_pick == com_pick:
            res_msg = "비겼습니다! 🤝"
        elif (player_pick == "가위" and com_pick == "보") or \
             (player_pick == "바위" and com_pick == "가위") or \
             (player_pick == "보" and com_pick == "바위"):
            status["player"] += 1
            res_msg = f"이겼습니다! 🎉 (컴퓨터: {com_pick})"
        else:
            status["computer"] += 1
            res_msg = f"졌습니다... 😢 (컴퓨터: {com_pick})"

        # 결과 업데이트
        result_text.value = res_msg
        score_text.value = f"현재 스코어 - 나: {status['player']} | 컴퓨터: {status['computer']}"

        # 최종 승패 확인
        if status["player"] == 3:
            result_text.value = "🎊 축하합니다! 최종 승리하셨습니다! 🎊"
            reset_button.visible = True
        elif status["computer"] == 3:
            result_text.value = "💀 컴퓨터가 최종 승리했습니다. 💀"
            reset_button.visible = True
            
        page.update()

    def restart_game():
        status["player"] = 0
        status["computer"] = 0
        result_text.value = "새 게임을 시작합니다!"
        score_text.value = "현재 스코어 - 나: 0 | 컴퓨터: 0"
        reset_button.visible = False
        page.update()

    # 4. 화면 레이아웃 배치
    page.add(
        ft.Column(
            [
                ft.Text("가위바위보 챔피언십", size=30, weight="bold"),
                ft.Row([
                    ft.ElevatedButton("✌️ 가위", on_click=lambda _: play("가위")),
                    ft.ElevatedButton("✊ 바위", on_click=lambda _: play("바위")),
                    ft.ElevatedButton("✋ 보", on_click=lambda _: play("보")),
                ], alignment=ft.MainAxisAlignment.CENTER),
                result_text,
                score_text,
                reset_button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

# 웹 브라우저 실행
ft.app(target=main, view=ft.AppView.WEB_BROWSER)