class ListADT:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.items = [None] * max_size
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

    def append(self, e):
        if self.isFull():
            print("가득 참")
            return
        self.items[self.size] = e
        self.size += 1

    def insert(self, pos, e):
        if self.isFull():
            print("가득 참")
            return
        if pos < 0 or pos > self.size:
            print("위치 오류")
            return

        for i in range(self.size, pos, -1):
            self.items[i] = self.items[i - 1]

        self.items[pos] = e
        self.size += 1

    def delete(self, pos):
        if self.isEmpty():
            print("비어있음")
            return None
        if pos < 0 or pos >= self.size:
            print("위치 오류")
            return None

        removed = self.items[pos]

        for i in range(pos, self.size - 1):
            self.items[i] = self.items[i + 1]

        self.items[self.size - 1] = None
        self.size -= 1

        return removed

    def getEntry(self, pos):
        if pos < 0 or pos >= self.size:
            print("위치 오류")
            return None
        return self.items[pos]

    def clear(self):
        for i in range(self.size):
            self.items[i] = None
        self.size = 0

    def find(self, item):
        for i in range(self.size):
            if self.items[i] == item:
                return i
        return -1

    def replace(self, pos, item):
        if pos < 0 or pos >= self.size:
            print("위치 오류")
            return
        self.items[pos] = item

    def sort(self):
        temp = self.items[:self.size]
        temp.sort()
        for i in range(self.size):
            self.items[i] = temp[i]

    def merge(self, lst):
        for e in lst:
            self.append(e)

    def display(self):
        print(self.items[:self.size])