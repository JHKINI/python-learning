class SetADT:

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.items = [None] * max_size
        self.size = 0

    def isEmpty(self):
        return self.size == 0


    def isFull(self):
        return self.size == self.max_size


    def contains(self, e):
        for i in range(self.size):
            if self.items[i] == e:
                return True
        return False

    def insert(self, e):
        if self.isFull():
            print("가득 참")
            return
        if self.contains(e):
            print("중복 불가")
            return
        self.items[self.size] = e
        self.size += 1
 
    def delete(self, e):
        for i in range(self.size):
            if self.items[i] == e:
                removed = self.items[i]
                for j in range(i, self.size - 1):
                    self.items[j] = self.items[j + 1]
                self.items[self.size - 1] = None
                self.size -= 1
                return removed
        return None

    def size_func(self):
        return self.size

    def display(self):
        print(self.items[:self.size])


    def union(self, setB):
        result = SetADT(self.max_size + setB.size)
        for i in range(self.size):
            result.insert(self.items[i])
        for i in range(setB.size):
            result.insert(setB.items[i])
        return result

    def intersect(self, setB):
        result = SetADT()
        for i in range(self.size):
            if setB.contains(self.items[i]):
                result.insert(self.items[i])
        return result

    def difference(self, setB):
        result = SetADT()
        for i in range(self.size):
            if not setB.contains(self.items[i]):
                result.insert(self.items[i])
        return result

    def equals(self, setB):
        if self.size != setB.size:
            return False
        for i in range(self.size):
            if not setB.contains(self.items[i]):
                return False
        return True


setA = SetADT()
setB = SetADT()

# 원소 삽입
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

# 원소 포함 여부
print("A에 B가 있는가?", setA.contains("B"))
print("A에 D가 있는가?", setA.contains("D"))

# 크기
print("A의 크기:", setA.size_func())

# 삭제
setA.delete("B")
print("B 삭제 후 A:")
setA.display()

# 합집합
union_set = setA.union(setB)
print("합집합:")
union_set.display()

# 교집합
intersect_set = setA.intersect(setB)
print("교집합:")
intersect_set.display()

# 차집합
difference_set = setA.difference(setB)
print("차집합 (A-B):")
difference_set.display()

# 집합 비교
print("A와 B가 같은가?", setA.equals(setB))

# 같은 집합 만들기
setC = SetADT()
setC.insert("A")
setC.insert("C")

print("집합 C:")
setC.display()

print("A와 C가 같은가?", setA.equals(setC))

# 공백 검사
print("A가 비어있는가?", setA.isEmpty())

# 모든 원소 삭제
setA.delete("A")
setA.delete("C")

print("모두 삭제 후 A:")
setA.display()

print("A가 비어있는가?", setA.isEmpty())