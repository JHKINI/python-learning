# 순차 탐색 / 이진 탐색
# coding: utf-8
def sequential_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

def binary_search(a, key):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

data = [10, 20, 30, 40, 50]
print('순차탐색 30:', sequential_search(data, 30))
print('이진탐색 40:', binary_search(data, 40))
