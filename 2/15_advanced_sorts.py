# 고급 정렬: 셸 / 병합 / 퀵 / 기수 정렬
# coding: utf-8

def shell_sort(a):
    a = a[:]
    gap = len(a) // 2
    while gap > 0:
        for i in range(gap, len(a)):
            temp = a[i]
            j = i
            while j >= gap and a[j-gap] > temp:
                a[j] = a[j-gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = [x for x in a[1:] if x <= pivot]
    right = [x for x in a[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def radix_sort(a):
    a = a[:]
    exp = 1
    max_val = max(a)
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in a:
            buckets[(num // exp) % 10].append(num)
        a = [num for bucket in buckets for num in bucket]
        exp *= 10
    return a

data = [170, 45, 75, 90, 802, 24, 2, 66]
print('셸:', shell_sort(data))
print('병합:', merge_sort(data))
print('퀵:', quick_sort(data))
print('기수:', radix_sort(data))
