class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.min = None

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = Node(val)
        if self.head.next:
            self.head.min = min(val, self.head.next.min)
        else:
            self.head.min = val

    def pop(self) -> None:
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min
        
