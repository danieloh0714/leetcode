# Time complexity: O(n)
# Space complexity: O(1)
def middle_node(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
