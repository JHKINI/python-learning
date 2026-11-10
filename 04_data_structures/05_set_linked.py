# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class SetADT:

    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return False  # 연결구조는 메모리만 있으면 계속 저장 가능

    def contains(self, e):
        current = self.head

        while current is not None:
            if current.data == e:
                return True
            current = current.link

        return False

    def insert(self, e):
        if self.contains(e):
            print("중복 불가")
            return

        new_node = Node(e)

        new_node.link = self.head
        self.head = new_node

        self.count += 1

    def delete(self, e):
        current = self.head
        previous = None

        while current is not None:

            if current.data == e:

                if previous is None:
                    self.head = current.link
                else:
                    previous.link = current.link

                self.count -= 1
                return e

            previous = current
            current = current.link

        return None

    def size_func(self):
        return self.count

    def display(self):

        current = self.head
        result = []

        while current is not None:
            result.append(current.data)
            current = current.link

        print(result)

    def union(self, setB):

        result = SetADT()

        current = self.head
        while current is not None:
            result.insert(current.data)
            current = current.link

        current = setB.head
        while current is not None:
            result.insert(current.data)
            current = current.link

        return result

    def intersect(self, setB):

        result = SetADT()

        current = self.head

        while current is not None:

            if setB.contains(current.data):
                result.insert(current.data)

            current = current.link

        return result

    def difference(self, setB):

        result = SetADT()

        current = self.head

        while current is not None:

            if not setB.contains(current.data):
                result.insert(current.data)

            current = current.link

        return result

    def equals(self, setB):

        if self.count != setB.count:
            return False

        current = self.head

        while current is not None:

            if not setB.contains(current.data):
                return False

            current = current.link

        return True


# 테스트

setA = SetADT()
setB = SetADT()

setA.insert("A")
setA.insert("B")
setA.insert("C")

setB.insert("B")
setB.insert("C")
setB.insert("D")

print("집합 A:")
setA.display()

print("집합 B:")
setB.display()

print("A에 B가 있는가?", setA.contains("B"))
print("A에 D가 있는가?", setA.contains("D"))

print("A의 크기:", setA.size_func())

setA.delete("B")

print("B 삭제 후 A:")
setA.display()

union_set = setA.union(setB)

print("합집합:")
union_set.display()

intersect_set = setA.intersect(setB)

print("교집합:")
intersect_set.display()

difference_set = setA.difference(setB)

print("차집합(A-B):")
difference_set.display()

print("A와 B가 같은가?", setA.equals(setB))