# Time complexity: O(n)
# Space complexity: O(1)
def reorder_list(head) -> None:
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    curr = slow.next
    slow.next = None
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    one, two = head, prev
    while two:
        temp_one, temp_two = one.next, two.next
        one.next = two
        two.next = temp_one
        one, two = temp_one, temp_two
