# Time complexity: O(n)
# Space complexity: O(1)
def remove_elements(head, val: int):
    dummy = ListNode(next=head)
    curr = dummy

    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next
