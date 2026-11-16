import bisect


def binary_search(items, target):         # O(log n); items must be sorted
    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            lo = mid + 1                  # target is in the right half
        else:
            hi = mid - 1                  # target is in the left half
    return -1


def lower_bound(items, target):
    """First index whose value is >= target (the insertion point)."""
    lo, hi = 0, len(items)                # note: hi is one past the end
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if items[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


nums = [3, 8, 15, 15, 15, 23, 42, 57]
print(binary_search(nums, 23))            # 5
print(binary_search(nums, 9))             # -1
print(lower_bound(nums, 15))              # 2  (first 15)
print(bisect.bisect_left(nums, 15))       # 2  (standard library equivalent)
