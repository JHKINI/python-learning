# -*- coding: utf-8 -*-
# 예제: 힙 응용 - 허프만 코드 생성 과정
# 최소 힙을 사용해 빈도수가 작은 두 값을 계속 합치는 예제

import heapq


def make_tree(freq):
    # 최소 힙 생성
    heap = []

    for n in freq:
        heapq.heappush(heap, n)

    # 값이 하나 남을 때까지 작은 값 2개를 꺼내 합침
    while len(heap) > 1:
        e1 = heapq.heappop(heap)
        e2 = heapq.heappop(heap)
        heapq.heappush(heap, e1 + e2)
        print("(%d + %d)" % (e1, e2))

    return heap[0]


# 실행 예시
if __name__ == "__main__":
    label = ["E", "T", "N", "I", "S"]
    freq = [15, 12, 8, 6, 4]

    print("문자:", label)
    print("빈도:", freq)
    print("합치는 과정:")
    result = make_tree(freq)
    print("최종 합:", result)
