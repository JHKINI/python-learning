
#맵응용: 단어장만들기
class SequentialMap:

    def __init__(self):
        self.table = []

    # 추가
    def insert(self, key, value):
        self.table.append((key, value))

    # 탐색
    def search(self, key):

        for k, v in self.table:
            if k == key:
                return v

        return None

    # 삭제
    def delete(self, key):

        for i in range(len(self.table)):

            if self.table[i][0] == key:
                self.table.pop(i)
                return

    # 출력
    def display(self):
        print(self.table)


# 실행 예시
map = SequentialMap()

map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('game', '게임')

map.display()

print(map.search('game'))

map.delete('game')

map.display()