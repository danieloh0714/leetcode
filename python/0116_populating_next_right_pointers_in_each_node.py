# Time complexity: O(n)
# Space complexity: O(1)
def connect(root):
    if not root: return root

    curr = root
    nxt = curr.left
    while nxt:
        curr.left.next = curr.right
        if curr.next:
            curr.right.next = curr.next.left
            curr = curr.next
        else:
            curr = nxt
            nxt = curr.left

    return root
