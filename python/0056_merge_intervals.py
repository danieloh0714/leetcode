# Time complexity: O(nlog(n))
# Space complexity: O(n)
def merge(intervals: list) -> list:
    sorted_intervals = sorted(intervals)

    ans = []
    for interval in sorted_intervals:
        start, end = interval
        if not ans or start > ans[-1][1]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], end)

    return ans
