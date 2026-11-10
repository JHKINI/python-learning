class 도서관리:
    def __init__(self):
        self.책목록={}
    def 책제목저장(self,제목,저자):
        self.책목록[제목]=저자
    def 검색하기(self,제목):
        if 제목 in self.책목록:
            return self.책목록.get(제목)
        else:
            return "책이 없습니다"
    def 출력하기(self):
        return self.책목록
    def 삭제하기(self,제목):
        if 제목 in self.책목록:
            del self.책목록[제목]
            return "삭제완료"
        else:
            return "삭제할 책이 없습니다"

book= 도서관리()
book.책제목저장("어린왕자","생텍쥐페리")
book.책제목저장("데미안","헤르만 헤세")

print(book.검색하기("어린왕자"))
print(book.검색하기("해리포터"))
print(book.출력하기())
print(book.삭제하기("데미안"))
