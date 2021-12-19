# Time complexity: O(n)
# Space complexity: O(1)
def insert(intervals: list, new_interval: list) -> list:
    ans = []
    
    merged = [new_interval[0], new_interval[1]]
    for i, interval in enumerate(intervals):
        start, end = interval
        if merged[1] < start:
            ans.append(merged)
            return ans + intervals[i:]
        if merged[0] > end:
            ans.append(interval)
        else:
            merged = [min(merged[0], start), max(merged[1], end)]

    ans.append(merged)

    return ans
