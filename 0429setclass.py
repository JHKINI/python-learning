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