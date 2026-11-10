class 전화번호부:
    def __init__(self):
        self.번호부 = {}
        self.즐겨찾기 = []
        self.차단 = []
    
    def 저장하기(self, 이름, 전화번호):
        self.번호부[이름] = 전화번호
    
    def 검색하기(self, 이름):
        return self.번호부.get(이름)
    
    def 전체출력(self):
        return self.번호부
    
    def 즐겨찾기추가(self, 이름):
        self.즐겨찾기.append(이름)

    def 즐겨찾기삭제(self, 이름):
        if 이름 in self.즐겨찾기:
            self.즐겨찾기.remove(이름)

    def 즐겨찾기목록(self):
        return self.즐겨찾기

    def 차단추가(self, 이름):
        self.차단.append(이름)

    def 차단삭제(self, 이름):
        if 이름 in self.차단:
            self.차단.remove(이름)

    def 차단목록(self):
        return self.차단

book = 전화번호부()

while True:
    메뉴 = input(

        "1:저장 2:검색 3:전체출력 4:즐겨찾기추가 5:즐겨찾기삭제 "

        "6:즐겨찾기목록 7:차단추가 8:차단삭제 9:차단목록 0:종료 >> "
    )
    if 메뉴 == "1":
        이름 = input("이름을 입력하세요: ")
        전화번호 = input("전화번호를 입력하세요: ")
        book.저장하기(이름, 전화번호)

    elif 메뉴 == "2":
        이름 = input("검색할 이름을 입력하세요: ")
        print(book.검색하기(이름))

    elif 메뉴 == "3":
        print(book.전체출력())

    elif 메뉴 == "4":
        이름 = input("즐겨찾기에 추가할 이름: ")
        book.즐겨찾기추가(이름)

    elif 메뉴 == "5":
        이름 = input("즐겨찾기에서 삭제할 이름: ")
        book.즐겨찾기삭제(이름)

    elif 메뉴 == "6":
        print(book.즐겨찾기목록())

    elif 메뉴 == "7":
        이름 = input("차단할 이름: ")
        book.차단추가(이름)

    elif 메뉴 == "8":
        이름 = input("차단 해제할 이름: ")
        book.차단삭제(이름)

    elif 메뉴 == "9":
        print(book.차단목록())

    elif 메뉴 == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다.")