import json
import flet as ft


class 전화번호부:
    def __init__(self):
        self.번호부 = {}
        self.즐겨찾기 = []
        self.차단 = []

    def 저장하기(self, 이름, 전화번호, 이메일, 회사명, 메모):
        이름 = 이름.strip()
        if not 이름:
            return "이름을 입력하세요"

        if 이름 in self.번호부:
            return "이미 존재하는 이름입니다"

        self.번호부[이름] = {
            "전화번호": 전화번호.strip(),
            "이메일": 이메일.strip(),
            "회사명": 회사명.strip(),
            "메모": 메모.strip()
        }
        return "저장 완료"

    def 수정하기(self, 이름, 전화번호, 이메일, 회사명, 메모):
        이름 = 이름.strip()
        if 이름 not in self.번호부:
            return "수정할 이름이 없습니다"

        self.번호부[이름] = {
            "전화번호": 전화번호.strip(),
            "이메일": 이메일.strip(),
            "회사명": 회사명.strip(),
            "메모": 메모.strip()
        }
        return "수정 완료"

    def 검색하기(self, 이름):
        이름 = 이름.strip()

        if not 이름:
            return self.번호부

        결과 = {}
        for key, value in self.번호부.items():
            if 이름 in key:
                if key in self.차단:
                    continue
                결과[key] = value

        if 결과:
            return 결과
        return "검색 결과가 없습니다"

    def 전체출력(self):
        return self.번호부

    def 이름순정렬(self):
        return dict(sorted(self.번호부.items()))

    def 즐겨찾기추가(self, 이름):
        이름 = 이름.strip()
        if 이름 not in self.번호부:
            return "번호부에 없는 이름입니다"
        if 이름 in self.즐겨찾기:
            return "이미 즐겨찾기에 있습니다"

        self.즐겨찾기.append(이름)
        return "즐겨찾기 추가 완료"

    def 즐겨찾기삭제(self, 이름):
        이름 = 이름.strip()
        if 이름 in self.즐겨찾기:
            self.즐겨찾기.remove(이름)
            return "즐겨찾기 삭제 완료"
        return "즐겨찾기에 없는 이름입니다"

    def 즐겨찾기목록(self):
        결과 = {}
        for 이름 in self.즐겨찾기:
            if 이름 in self.번호부:
                결과[이름] = self.번호부[이름]
        return 결과

    def 차단추가(self, 이름):
        이름 = 이름.strip()
        if 이름 not in self.번호부:
            return "번호부에 없는 이름입니다"
        if 이름 in self.차단:
            return "이미 차단된 이름입니다"

        self.차단.append(이름)
        return "차단 완료"

    def 차단해제(self, 이름):
        이름 = 이름.strip()
        if 이름 in self.차단:
            self.차단.remove(이름)
            return "차단 해제 완료"
        return "차단 해제할 이름이 없습니다"

    def 차단목록(self):
        결과 = {}
        for 이름 in self.차단:
            if 이름 in self.번호부:
                결과[이름] = self.번호부[이름]
        return 결과

    def 삭제하기(self, 이름):
        이름 = 이름.strip()
        if 이름 in self.번호부:
            del self.번호부[이름]

            if 이름 in self.즐겨찾기:
                self.즐겨찾기.remove(이름)
            if 이름 in self.차단:
                self.차단.remove(이름)

            return "삭제 완료"
        return "삭제할 번호가 없습니다"

    def 파일저장(self):
        with open("phonebook.json", "w", encoding="utf-8") as f:
            data = {
                "번호부": self.번호부,
                "즐겨찾기": self.즐겨찾기,
                "차단": self.차단
            }
            json.dump(data, f, ensure_ascii=False, indent=2)
        return "파일 저장 완료"

    def 파일불러오기(self):
        try:
            with open("phonebook.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.번호부 = data.get("번호부", {})
                self.즐겨찾기 = data.get("즐겨찾기", [])
                self.차단 = data.get("차단", [])
            return "파일 불러오기 완료"
        except FileNotFoundError:
            return "저장된 파일이 없습니다"


def main(page: ft.Page):
    book = 전화번호부()

    # 샘플 데이터
    book.저장하기("김철수", "010-1111-2222", "kim@test.com", "ABC상사", "첫 고객")
    book.저장하기("박영희", "010-3333-4444", "park@test.com", "한빛무역", "중요 거래처")

    page.title = "고객 연락처 관리 앱"
    page.window_width = 1200
    page.window_height = 900
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.Colors.GREY_100

    page.appbar = ft.AppBar(
        title=ft.Text("전화번호부", weight=ft.FontWeight.BOLD),
        bgcolor=ft.Colors.BLUE_100
    )

    이름 = ft.TextField(label="이름", width=250)
    전화번호 = ft.TextField(label="전화번호", width=250)
    이메일 = ft.TextField(label="이메일", width=250)
    회사명 = ft.TextField(label="회사명", width=250)
    메모 = ft.TextField(label="메모", width=500, multiline=True, min_lines=2, max_lines=4)

    검색어 = ft.TextField(label="이름 검색", hint_text="부분검색 가능", width=300)

    상태메시지 = ft.Text("준비 완료", size=15, weight=ft.FontWeight.BOLD)
    결과영역 = ft.Column()

    def 카드(제목, 내용들):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(제목, size=20, weight=ft.FontWeight.BOLD),
                    *내용들
                ],
                spacing=12
            ),
            padding=20,
            border_radius=16,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(1, ft.Colors.GREY_300)
        )

    def 상태표시(msg):
        상태메시지.value = msg
        page.update()

    def 입력초기화():
        이름.value = ""
        전화번호.value = ""
        이메일.value = ""
        회사명.value = ""
        메모.value = ""

    def 입력채우기(이름값):
        if 이름값 not in book.번호부:
            상태표시("해당 이름이 없습니다")
            return

        정보 = book.번호부[이름값]
        이름.value = 이름값
        전화번호.value = 정보.get("전화번호", "")
        이메일.value = 정보.get("이메일", "")
        회사명.value = 정보.get("회사명", "")
        메모.value = 정보.get("메모", "")
        상태표시("수정할 데이터를 불러왔습니다")
        page.update()

    def 결과표시(data):
        결과영역.controls.clear()

        if isinstance(data, str):
            결과영역.controls.append(
                ft.Text(data, size=16, color=ft.Colors.RED_700)
            )
            page.update()
            return

        if not data:
            결과영역.controls.append(
                ft.Text("데이터가 없습니다", size=16)
            )
            page.update()
            return

        rows = []
        for 이름값, 정보 in data.items():
            즐겨찾기표시 = "O" if 이름값 in book.즐겨찾기 else ""
            차단표시 = "O" if 이름값 in book.차단 else ""

            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(이름값, weight=ft.FontWeight.BOLD),
                            on_tap=lambda e, n=이름값: 입력채우기(n)
                        ),
                        ft.DataCell(ft.Text(정보.get("전화번호", ""))),
                        ft.DataCell(ft.Text(정보.get("이메일", ""))),
                        ft.DataCell(ft.Text(정보.get("회사명", ""))),
                        ft.DataCell(ft.Text(정보.get("메모", ""))),
                        ft.DataCell(ft.Text(즐겨찾기표시)),
                        ft.DataCell(ft.Text(차단표시)),
                    ]
                )
            )

        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("이름")),
                ft.DataColumn(ft.Text("전화번호")),
                ft.DataColumn(ft.Text("이메일")),
                ft.DataColumn(ft.Text("회사명")),
                ft.DataColumn(ft.Text("메모")),
                ft.DataColumn(ft.Text("즐겨찾기")),
                ft.DataColumn(ft.Text("차단")),
            ],
            rows=rows,
            column_spacing=20,
            horizontal_margin=10,
            heading_row_color=ft.Colors.BLUE_50,
        )

        결과영역.controls.append(
            ft.Text("이름 칸을 클릭하면 수정용으로 불러옵니다.", size=14)
        )
        결과영역.controls.append(table)
        page.update()

    def 저장(e):
        msg = book.저장하기(
            이름.value,
            전화번호.value,
            이메일.value,
            회사명.value,
            메모.value
        )
        상태표시(msg)
        if msg == "저장 완료":
            입력초기화()
            결과표시(book.전체출력())

    def 수정(e):
        msg = book.수정하기(
            이름.value,
            전화번호.value,
            이메일.value,
            회사명.value,
            메모.value
        )
        상태표시(msg)
        if msg == "수정 완료":
            결과표시(book.전체출력())

    def 검색(e):
        결과 = book.검색하기(검색어.value)
        결과표시(결과)
        상태표시("검색 완료")

    def 전체보기(e):
        결과표시(book.전체출력())
        상태표시("전체 출력 완료")

    def 이름정렬보기(e):
        결과표시(book.이름순정렬())
        상태표시("이름순 정렬 완료")

    def 즐겨찾기만보기(e):
        결과표시(book.즐겨찾기목록())
        상태표시("즐겨찾기 목록 출력 완료")

    def 차단목록보기(e):
        결과표시(book.차단목록())
        상태표시("차단 목록 출력 완료")

    def 즐겨찾기추가(e):
        msg = book.즐겨찾기추가(검색어.value)
        상태표시(msg)
        결과표시(book.전체출력())

    def 즐겨찾기삭제(e):
        msg = book.즐겨찾기삭제(검색어.value)
        상태표시(msg)
        결과표시(book.전체출력())

    def 차단추가(e):
        msg = book.차단추가(검색어.value)
        상태표시(msg)
        결과표시(book.전체출력())

    def 차단해제(e):
        msg = book.차단해제(검색어.value)
        상태표시(msg)
        결과표시(book.전체출력())

    def 파일저장(e):
        msg = book.파일저장()
        상태표시(msg)

    def 파일불러오기(e):
        msg = book.파일불러오기()
        상태표시(msg)
        결과표시(book.전체출력())

    def 삭제확인(e):
        이름값 = 검색어.value.strip()

        if not 이름값:
            상태표시("삭제할 이름을 검색창에 입력하세요")
            return

        def 확인삭제(ev):
            msg = book.삭제하기(이름값)
            상태표시(msg)
            결과표시(book.전체출력())
            page.close(dialog)

        def 취소(ev):
            page.close(dialog)

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("삭제 확인"),
            content=ft.Text(f"{이름값}을(를) 삭제하시겠습니까?"),
            actions=[
                ft.TextButton("취소", on_click=취소),
                ft.TextButton("삭제", on_click=확인삭제),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.open(dialog)

    상태배너 = ft.Container(
        content=상태메시지,
        padding=12,
        border_radius=12,
        bgcolor=ft.Colors.BLUE_50,
        border=ft.border.all(1, ft.Colors.BLUE_100),
    )

    입력카드 = 카드(
        "입력 / 수정",
        [
            ft.Row([이름, 전화번호], wrap=True),
            ft.Row([이메일, 회사명], wrap=True),
            메모,
            ft.Row(
                [
                    ft.Button("저장", on_click=저장),
                    ft.Button("수정", on_click=수정),
                    ft.OutlinedButton(
                        "입력 초기화",
                        on_click=lambda e: (입력초기화(), page.update())
                    ),
                ],
                wrap=True
            ),
        ]
    )

    관리카드 = 카드(
        "검색 / 관리",
        [
            검색어,
            ft.Row(
                [
                    ft.Button("검색", on_click=검색),
                    ft.Button("전체보기", on_click=전체보기),
                    ft.Button("이름순 정렬", on_click=이름정렬보기),
                ],
                wrap=True
            ),
            ft.Row(
                [
                    ft.OutlinedButton("즐겨찾기 추가", on_click=즐겨찾기추가),
                    ft.OutlinedButton("즐겨찾기 삭제", on_click=즐겨찾기삭제),
                    ft.OutlinedButton("차단 추가", on_click=차단추가),
                    ft.OutlinedButton("차단 해제", on_click=차단해제),
                ],
                wrap=True
            ),
            ft.Row(
                [
                    ft.OutlinedButton("즐겨찾기만 보기", on_click=즐겨찾기만보기),
                    ft.OutlinedButton("차단목록 보기", on_click=차단목록보기),
                    ft.Button("삭제", on_click=삭제확인),
                ],
                wrap=True
            ),
            ft.Row(
                [
                    ft.TextButton("파일저장", on_click=파일저장),
                    ft.TextButton("파일불러오기", on_click=파일불러오기),
                ]
            ),
            상태배너,
        ]
    )

    결과카드 = ft.Container(
        content=ft.Column(
            [
                ft.Text("연락처 목록", size=22, weight=ft.FontWeight.BOLD),
                결과영역
            ],
            spacing=12
        ),
        padding=20,
        border_radius=16,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_300)
    )

    page.add(
       
        입력카드,
        관리카드,
        결과카드,
    )

    결과표시(book.전체출력())


ft.app(target=main)