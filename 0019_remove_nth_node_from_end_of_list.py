# Time complexity: O(n)
# Space complexity: O(1)
def remove_nth_from_end(head, n: int):
    one, two = head, head
    for _ in range(n):
        two = two.next

    if not two: return one.next

    while two.next:
        one, two = one.next, two.next

    one.next = one.next.next
    return head
