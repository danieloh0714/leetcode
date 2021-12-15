# Time complexity: O(n)
# Space complexity: O(1)
def swap_pairs(head):
    if not head or not head.next: return head

    dummy = prev = ListNode()
    curr = head
    while curr and curr.next:
        one, two = curr, curr.next
        one.next = two.next
        two.next = one
        prev.next = two
        prev = one
        curr = one.next

    return dummy.next
