# Time complexity: O(m+n)
# Space complexity: O(m+n)
def merge_two_lists(list1, list2):
    merged = curr = ListNode()
    
    one, two = list1, list2
    while one or two:
        one_val = one.val if one else float('inf')
        two_val = two.val if two else float('inf')
        if one_val < two_val:
            curr.next = ListNode(one_val)
            one = one.next
        else:
            curr.next = ListNode(two_val)
            two = two.next
        curr = curr.next

    return merged.next
