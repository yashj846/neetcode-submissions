class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode = Node(value)
        lastNode = self.tail.prev

        lastNode.next = newNode
        newNode.prev = lastNode
        newNode.next = self.tail 
        self.tail.prev = newNode 
        

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        firstNode = self.head.next 
        
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = firstNode
        firstNode.prev = newNode   

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        targetNode = self.tail.prev
        value = targetNode.value

        prevNode = targetNode.prev

        prevNode.next = self.tail
        self.tail.prev = prevNode

        return value
        

    def popleft(self) -> int:

        if self.isEmpty():
            return -1

        targetNode = self.head.next
        value = targetNode.value

        nextNode = targetNode.next

        nextNode.prev = self.head
        self.head.next = nextNode

        return value
        
