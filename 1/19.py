def quick_sort(a, L, R):
    left, right = L, R
    pivot = a[(L + R) // 2]          # 가운데 값을 피벗으로 선택

    while left <= right:             # 좌우 포인터가 교차할 때까지 반복
        while a[left] < pivot:       # 피벗보다 작은 값은 왼쪽으로
            left += 1
        while a[right] > pivot:      # 피벗보다 큰 값은 오른쪽으로
            right -= 1

        if left <= right:            # 교차 전이면 교환
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1

    # 재귀로 왼쪽과 오른쪽 부분을 정렬
    if L < right:
        quick_sort(a, L, right)
    if left < R:
        quick_sort(a, left, R)
    
arr = [6, 2, 3, 4, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)   # [1, 2, 3, 4, 6]