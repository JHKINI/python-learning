# -*- coding: utf-8 -*-
class Set:
    def __init__(self):
        self.items = []

    # 쉬운 방법
    def union_easy(self, setB):

        setC = Set()
        setC.items = list(self.items)

        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)

        return setC

    # 빠른 방법
    def union_fast(self, setB):

        newSet = Set()

        a = 0
        b = 0

        while a < len(self.items) and b < len(setB.items):

            valueA = self.items[a]
            valueB = setB.items[b]

            if valueA < valueB:
                newSet.items.append(valueA)
                a += 1

            elif valueA > valueB:
                newSet.items.append(valueB)
                b += 1

            else:
                newSet.items.append(valueA)
                a += 1
                b += 1

        while a < len(self.items):
            newSet.items.append(self.items[a])
            a += 1

        while b < len(setB.items):
            newSet.items.append(setB.items[b])
            b += 1

        return newSet


# 실행 예시
if __name__ == "__main__":
    A = Set()
    A.items = [1, 3, 5]

    B = Set()
    B.items = [2, 3, 4]

    print(A.union_easy(B).items)
    print(A.union_fast(B).items)