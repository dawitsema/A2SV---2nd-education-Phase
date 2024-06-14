class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        for i in range(index):
            if not temp:
                return -1
            temp = temp.next
        return temp.val if temp else -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        newNode = Node(val)

        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return

        for i in range(index - 1):
            if not temp:
                return
            temp = temp.next

        if temp:
            newNode.next = temp.next
            temp.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        if index == 0:
            self.head = temp.next
            return

        for i in range(index - 1):
            if not temp:
                return
            temp = temp.next

        if temp and temp.next:
            temp.next = temp.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)