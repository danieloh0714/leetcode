class Node:

    def __init__(self, val=0, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self) -> None:
        self.size = 0
        self.pre_head = Node()
        self.post_tail = Node()

        self.pre_head.next = self.post_tail
        self.post_tail.prev = self.pre_head

    def get(self, index: int) -> int:
        if index >= self.size: return -1

        curr = self.pre_head
        for _ in range(index+1):
            curr = curr.next

        return curr.val

    def add_at_head(self, val: int) -> None:
        node = Node(val=val)
        node.next = self.pre_head.next
        node.prev = self.pre_head
        self.pre_head.next.prev = node
        self.pre_head.next = node
        
        self.size += 1

    def add_at_tail(self, val: int) -> None:
        node = Node(val=val)
        node.prev = self.post_tail.prev
        node.next = self.post_tail
        self.post_tail.prev.next = node
        self.post_tail.prev = node

        self.size += 1

    def add_at_index(self, index: int, val: int) -> None:
        if index > self.size: return
        if index == self.size:
            self.add_at_tail(val)
        elif index == 0:
            self.add_at_head(val)
        else:
            node = Node(val=val)
            curr = self.pre_head
            for _ in range(index+1):
                curr = curr.next

            node.prev = curr.prev
            curr.prev.next = node
            node.next = curr
            curr.prev = node

            self.size += 1

    def delete_at_index(self, index: int) -> None:
        if index >= self.size: return

        curr = self.pre_head
        for _ in range(index+1):
            curr = curr.next
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        self.size -= 1
