# 선택 정렬 / 삽입 정렬 / 버블 정렬
# coding: utf-8
def selection_sort(a):
    a = a[:]
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def bubble_sort(a):
    a = a[:]
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

data = [5, 3, 8, 1, 2]
print('원본:', data)
print('선택:', selection_sort(data))
print('삽입:', insertion_sort(data))
print('버블:', bubble_sort(data))
