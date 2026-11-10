class ListADT:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.items = [None] * max_size
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def insert(self, pos, e):
        if self.isFull():
            print("가득 참")
            return

        for i in range(self.size, pos, -1):
            self.items[i] = self.items[i - 1]

        self.items[pos] = e
        self.size += 1

    def delete(self, pos):
        if self.isEmpty():
            return None

        removed = self.items[pos]

        for i in range(pos, self.size - 1):
            self.items[i] = self.items[i + 1]

        self.items[self.size - 1] = None
        self.size -= 1

        return removed

    def replace(self, pos, e):
        self.items[pos] = e

    def getEntry(self, pos):
        return self.items[pos]

    def display(self):
        for i in range(self.size):
            print(f"{i}: {self.items[i]}")


# 라인 편집기
def line_editor():
    doc = ListADT(100)

    while True:
        cmd = input("명령(i,d,r,p,l,s,q): ")

        if cmd == 'i':
            pos = int(input("행 번호: "))
            text = input("내용: ")
            doc.insert(pos, text)

        elif cmd == 'd':
            pos = int(input("행 번호: "))
            doc.delete(pos)

        elif cmd == 'r':
            pos = int(input("행 번호: "))
            text = input("내용: ")
            doc.replace(pos, text)

        elif cmd == 'p':
            print("\n[현재 문서]")
            doc.display()
            print()

        elif cmd == 'l':
            try:
                f = open("test.txt", "r")
                doc = ListADT(100)
                for line in f:
                    doc.insert(doc.size, line.strip())
                f.close()
                print("파일 로드 완료")
            except:
                print("파일 없음")

        elif cmd == 's':
            f = open("test.txt", "w")
            for i in range(doc.size):
                f.write(doc.getEntry(i) + "\n")
            f.close()
            print("저장 완료")

        elif cmd == 'q':
            print("종료")
            break

        else:
            print("잘못된 명령")


# 실행
line_editor()