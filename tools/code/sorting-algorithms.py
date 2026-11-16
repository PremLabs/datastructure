def bubble_sort(a):                       # O(n^2), stable, in place
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:                   # already sorted: stop early
            break
    return a

def selection_sort(a):                    # O(n^2), not stable, in place
    for i in range(len(a) - 1):
        smallest = i
        for j in range(i + 1, len(a)):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]
    return a

def insertion_sort(a):                    # O(n^2) worst, O(n) if nearly sorted, stable
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(a):                        # O(n log n) always, stable, O(n) extra space
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:           # <= keeps equal items in order (stable)
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    return merged + left[i:] + right[j:]

def quick_sort(a, lo=0, hi=None):         # O(n log n) average, O(n^2) worst, in place
    if hi is None:
        hi = len(a) - 1
    if lo < hi:
        pivot, i = a[hi], lo
        for j in range(lo, hi):           # Lomuto partition
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        quick_sort(a, lo, i - 1)
        quick_sort(a, i + 1, hi)
    return a


data = [38, 27, 43, 3, 9, 82, 10]
for sort in (bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort):
    print(sort.__name__, sort(data[:]))   # each prints [3, 9, 10, 27, 38, 43, 82]
