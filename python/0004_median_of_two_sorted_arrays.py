# Time complexity: O(log(m+n))
# Space complexity: O(1)
def find_median_sorted_arrays(nums1: list, nums2: list) -> float:
    A, B = nums1, nums2
    if len(B) < len(A):
        A, B = B, A

    length = len(A)+len(B)
    half = length//2

    li, ri = 0, len(A)-1
    while True:
        i = (li+ri)//2
        j = half-(i+1)-1

        left_one = A[i] if i >= 0 else float('-inf')
        right_one = A[i+1] if i+1 < len(A) else float('inf')
        left_two = B[j] if j >= 0 else float('-inf')
        right_two = B[j+1] if j+1 < len(B) else float('inf')

        if left_one <= right_two and left_two <= right_one:
            if length%2 == 0:
                return (max(left_one, left_two)+min(right_one, right_two))/2
            return min(right_one, right_two)
        if left_one > right_two:
            ri = i-1
        else:
            li = i+1
