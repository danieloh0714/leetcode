class Node:

    def __init__(self, key=-1, val=-1, next=None, prev=None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = dict[int, Node]() # key: Node
        self.pre_head = Node()
        self.post_tail = Node()
        self.pre_head.next = self.post_tail
        self.post_tail.prev = self.pre_head

    def insert_at_end(self, node: Node) -> None:
        self.cache[node.key] = node

        tail = self.post_tail.prev
        tail.next = node
        node.prev = tail
        self.post_tail.prev = node
        node.next = self.post_tail

    def remove(self, node: Node) -> None:
        del self.cache[node.key]

        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        node = self.cache[key]
        self.remove(node)
        self.insert_at_end(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key=key, val=value)
        self.insert_at_end(self.cache[key])

        if len(self.cache) > self.capacity:
            self.remove(self.pre_head.next)
