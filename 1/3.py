# -*- coding: utf-8 -*-
#간단한탐색:순차탐색
def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i].key == key:
            return i
    return None
# 재귀 방식 이진 탐색
def binary_search(A, key, low, high):
    if (low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif (key < A[middle]):
            return binary_search(A, key, low, middle - 1)
        else:
            return binary_search(A, key, middle + 1, high)
    return None


# 반복문 방식 이진 탐색
def binary_search_iter(A, key, low, high):
    while (low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif (key > A[middle]):
            low = middle + 1
        else:
            high = middle - 1
    return None


# 실행 예시
if __name__ == "__main__":
    A = [2, 6, 11, 18, 22, 27, 34, 38]

    print(binary_search(A, 27, 0, len(A)-1))
    print(binary_search_iter(A, 27, 0, len(A)-1))