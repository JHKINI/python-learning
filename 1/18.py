# -*- coding: utf-8 -*-
# 예제: 힙정렬(Heap Sort)
# 최대 힙을 만든 뒤, 최댓값을 뒤쪽으로 보내며 오름차순 정렬


def downHeap(arr, i, size):
    # i 위치의 값을 아래로 내리며 최대 힙 조건 유지
    while 2 * i + 1 < size:
        left = 2 * i + 1
        right = 2 * i + 2
        larger = left

        if right < size and arr[right] > arr[left]:
            larger = right

        if arr[i] >= arr[larger]:
            break

        arr[i], arr[larger] = arr[larger], arr[i]
        i = larger


def heap_sort(arr):
    arr = arr[:]
    n = len(arr)

    # 1단계: 리스트 전체를 최대 힙으로 만들기
    for i in range(n // 2 - 1, -1, -1):
        downHeap(arr, i, n)

    # 2단계: 루트 최댓값을 뒤로 보내고 다시 힙 만들기
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        downHeap(arr, 0, end)

    return arr


# 실행 예시
if __name__ == "__main__":
    data = [5, 3, 8, 1, 2, 7, 4]
    print("원본:", data)
    print("힙정렬:", heap_sort(data))
