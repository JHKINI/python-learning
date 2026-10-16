class 도서관리:
    def __init__(self):
        self.책목록 = {}

    def 저장하기(self, 제목, 저자):
        self.책목록[제목]=저자

    def 검색하기(self, 제목):
        if 제목 in self.책목록:
            return self.책목록.get(제목)  
        else:
            return "책이 없습니다"


class 도서프로그램:
    def __init__(self):
        self.book = 도서관리()

    def 실행하기(self):
        while True:
            메뉴 = input("1:저장 2:검색 0:종료 >> ")

            if 메뉴 == "1":
                제목 = input("책 제목: ")
                저자 = input("저자: ")
                self.book.get(제목,저자)

            elif 메뉴 == "2":
                제목 = input("검색할 책 제목: ")
                print(self.book.검색하기(제목))   # 5️⃣

            elif 메뉴 == "0":
                break


app = 도서프로그램()
app.실행하기()