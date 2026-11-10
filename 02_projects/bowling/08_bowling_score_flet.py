
import random
import flet as ft


# ==========================================
# 1. 볼링 게임 생성
# ==========================================

def 볼링게임_생성():

    프레임당쓰러진핀 = []

    # 1~9프레임
    for _ in range(9):

        첫번째 = random.randint(0, 10)

        if 첫번째 == 10:
            두번째 = 0
        else:
            두번째 = random.randint(0, 10 - 첫번째)

        프레임당쓰러진핀.append([첫번째, 두번째])

    # 10프레임
    첫번째 = random.randint(0, 10)

    if 첫번째 == 10:

        두번째 = random.randint(0, 10)
        세번째 = random.randint(0, 10)

    else:

        두번째 = random.randint(0, 10 - 첫번째)

        if 첫번째 + 두번째 == 10:
            세번째 = random.randint(0, 10)
        else:
            세번째 = 0

    프레임당쓰러진핀.append([첫번째, 두번째, 세번째])

    return 프레임당쓰러진핀


# ==========================================
# 2. 점수 계산
# ==========================================

def 점수_계산(프레임당쓰러진핀):

    # 전체 투구 결과를 하나의 리스트로 변환
    투구결과 = []

    for 프레임 in 프레임당쓰러진핀:
        투구결과.extend(프레임)

    프레임당점수 = []
    누적점수 = []

    투구인덱스 = 0
    누적합계 = 0

    for i in range(10):

        현재프레임 = 프레임당쓰러진핀[i]

        if i == 9:

            점수 = sum(현재프레임)

        elif 현재프레임[0] == 10:

            # 스트라이크: 다음 2구 보너스
            점수 = 10 + 투구결과[투구인덱스 + 1] + 투구결과[투구인덱스 + 2]

            투구인덱스 += 1

        elif sum(현재프레임) == 10:

            # 스페어: 다음 1구 보너스
            점수 = 10 + 투구결과[투구인덱스 + 2]

            투구인덱스 += 2

        else:

            # 오픈 프레임
            점수 = sum(현재프레임)

            투구인덱스 += 2

        프레임당점수.append(점수)

        누적합계 += 점수
        누적점수.append(누적합계)

    return 프레임당점수, 누적점수


# ==========================================
# 3. 투구 결과 표시
# ==========================================

def 투구_표시(프레임, 번호):

    첫번째 = 프레임[0]
    두번째 = 프레임[1]

    if 번호 == 9:

        세번째 = 프레임[2]

        if 첫번째 == 10:
            표시1 = "X"
        else:
            표시1 = str(첫번째)

        if 첫번째 == 10:

            표시2 = "X" if 두번째 == 10 else str(두번째)
            표시3 = "X" if 세번째 == 10 else str(세번째)

        elif 첫번째 + 두번째 == 10:

            표시2 = "/"
            표시3 = "X" if 세번째 == 10 else str(세번째)

        else:

            표시2 = str(두번째)
            표시3 = "-"

        return [표시1, 표시2, 표시3]

    if 첫번째 == 10:
        return ["X", "-"]

    elif 첫번째 + 두번째 == 10:
        return [str(첫번째), "/"]

    else:
        return [
            str(첫번째) if 첫번째 != 0 else "-",
            str(두번째) if 두번째 != 0 else "-"
        ]


# ==========================================
# 4. Flet 화면 구성
# ==========================================

def main(page: ft.Page):

    page.title = "볼링 게임 점수판"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 25
    page.bgcolor = "#F3F5F9"

    def 게임_실행(e=None):

        프레임당쓰러진핀 = 볼링게임_생성()

        프레임당점수, 누적점수 = 점수_계산(
            프레임당쓰러진핀
        )

        프레임카드 = []

        for i in range(10):

            표시 = 투구_표시(
                프레임당쓰러진핀[i], i
            )

            # 투구 결과 표시
            투구컨트롤 = ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            값,
                            size=17,
                            weight=ft.FontWeight.BOLD,
                            color="#2563EB"
                        ),
                        width=27,
                        height=30,
                        alignment=ft.Alignment.CENTER,
                        bgcolor="#EFF6FF",
                        border_radius=5
                    )
                    for 값 in 표시
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=3
            )

            카드 = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            f"{i + 1} 프레임",
                            size=15,
                            weight=ft.FontWeight.BOLD
                        ),

                        투구컨트롤,

                        ft.Divider(),

                        ft.Text("프레임 점수", size=11, color="#64748B"),

                        ft.Text(
                            str(프레임당점수[i]),
                            size=21,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text("누적 점수", size=11, color="#64748B"),

                        ft.Text(
                            str(누적점수[i]),
                            size=17,
                            weight=ft.FontWeight.BOLD,
                            color="#2563EB"
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=7
                ),
                width=125,
                padding=10,
                bgcolor="white",
                border_radius=10,
                border=ft.Border.all(1, "#DCE3ED")
            )

            프레임카드.append(카드)

        page.controls.clear()

        page.add(

            ft.Text(
                "🎳 BOWLING GAME",
                size=30,
                weight=ft.FontWeight.BOLD,
                color="#1E293B"
            ),

            ft.Text(
                "랜덤 볼링 게임 점수판",
                size=15,
                color="#64748B"
            ),

            ft.Container(height=10),

            ft.Button(
            content="새 게임 시작",
            icon=ft.Icons.REFRESH,
            on_click=게임_실행,
            bgcolor="#2563EB",
            color="white"
            ),

            ft.Container(height=15),

            ft.Text(
                "FRAME SCORE BOARD",
                size=19,
                weight=ft.FontWeight.BOLD
            ),

            ft.Row(
                controls=프레임카드,
                wrap=True,
                spacing=10,
                run_spacing=10
            ),

            ft.Container(height=15),

            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "FINAL SCORE",
                            size=16,
                            color="#CBD5E1"
                        ),

                        ft.Text(
                            f"{누적점수[9]} 점",
                            size=42,
                            weight=ft.FontWeight.BOLD,
                            color="white"
                        ),

                        ft.Text(
                            "10프레임 경기 완료",
                            size=13,
                            color="#CBD5E1"
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8
                ),
                padding=25,
                bgcolor="#1E293B",
                border_radius=15,
                alignment=ft.Alignment.CENTER
            )
        )

        page.update()

    # 최초 실행
    게임_실행()


# ==========================================
# 5. 프로그램 실행
# ==========================================

ft.run(main)
