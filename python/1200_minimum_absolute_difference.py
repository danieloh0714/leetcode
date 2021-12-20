# Time complexity: O(nlog(n))
# Space complexity: O(n)
def minimum_abs_difference(arr: list) -> list:
    sorted_arr = sorted(arr)

    ans = []

    min_diff = float('inf')
    for i in range(1, len(sorted_arr)):
        pair = [sorted_arr[i-1], sorted_arr[i]]
        diff = pair[1]-pair[0]
        if diff < min_diff:
            min_diff = diff
            ans = [pair]
        elif diff == min_diff:
            ans.append(pair)

    return ans
