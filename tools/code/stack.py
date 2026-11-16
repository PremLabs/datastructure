class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):                # O(1) amortised
        self._items.append(value)

    def pop(self):                        # O(1)
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):                       # O(1)
        if not self._items:
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self):
        return not self._items


def is_balanced(text):
    """Classic stack problem: are the brackets in text balanced?"""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    for ch in text:
        if ch in "([{":
            stack.push(ch)
        elif ch in pairs:
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()


print(is_balanced("{[()]}"))              # True
print(is_balanced("([)]"))                # False
