def selection_sort(A):
    n = len(A)

    for i in range(n-1):
        min_idx = i

        for j in range(i+1, n):
            if A[j] < A[min_idx]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]

    return A


# 테스트
arr = [5, 3, 8, 4, 9, 1, 6]
print(selection_sort(arr))