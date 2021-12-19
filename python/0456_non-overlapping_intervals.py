# Time complexity: O(nlog(n))
# Space complexity: O(n)
def erase_overlap_intervals(intervals: list) -> int:
    sorted_intervals = sorted(intervals, key=lambda interval: interval[1])

    ans = 0
    curr_end = float('-inf')
    for start, end in sorted_intervals:
        if start < curr_end:
            ans += 1
        else:
            curr_end = end

    return ans
