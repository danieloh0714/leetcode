# Time complexity: O(max(m, n))
# Space complexity: O(max(m, n))
def add_two_numbers(l1, l2):
    dummy = curr = ListNode()

    carry = 0
    one, two = l1, l2
    while one or two or carry:
        one_val = one.val if one else 0
        two_val = two.val if two else 0
        val = one_val+two_val+carry
        carry = 0
        if val >= 10:
            carry = 1
            val -= 10
        curr.next = ListNode(val)
        curr = curr.next
        one = one.next if one else one
        two = two.next if two else two

    return dummy.next
