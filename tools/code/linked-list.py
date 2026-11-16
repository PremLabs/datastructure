class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):           # O(1)
        self.head = Node(value, self.head)

    def add_last(self, value):            # O(n) without a tail pointer
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def remove(self, value):              # O(n) to find, O(1) to unlink
        dummy = Node(None, self.head)     # dummy node removes the head special case
        prev = dummy
        while prev.next and prev.next.value != value:
            prev = prev.next
        if prev.next is None:
            return False
        prev.next = prev.next.next
        self.head = dummy.next
        return True

    def reverse(self):                    # O(n) time, O(1) space
        prev, current = None, self.head
        while current:
            current.next, prev, current = prev, current, current.next
        self.head = prev

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


items = LinkedList()
for v in (3, 15):
    items.add_last(v)
items.add_first(8)                        # 8 -> 3 -> 15
items.remove(3)                           # 8 -> 15
items.reverse()                           # 15 -> 8
print(list(items))
