def first_item(items):            # O(1): one step, whatever the size
    return items[0]

def contains(items, target):      # O(n): may look at every item
    for item in items:
        if item == target:
            return True
    return False

def has_duplicate(items):         # O(n^2): every pair is compared
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False

def has_duplicate_fast(items):    # O(n) time, O(n) extra space
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False

def halvings(n):                  # O(log n): n is halved each loop
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps

print(halvings(1_000_000))        # 19
print(has_duplicate_fast([3, 1, 4, 1]))  # True
