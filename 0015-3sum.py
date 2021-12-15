# Time complexity: O(n^2)
# Space complexity: O(n)
def three_sum(nums: list) -> list:
    triplets = []

    sorted_nums = sorted(nums)
    for li in range(len(sorted_nums)-2):
        left = sorted_nums[li]
        if li > 0 and left == sorted_nums[li-1]: continue
        mi, ri = li+1, len(sorted_nums)-1
        while mi < ri:
            middle, right = sorted_nums[mi], sorted_nums[ri]
            curr = left+middle+right
            if curr == 0:
                triplets.append([left, middle, right])
                mi += 1
                while mi < ri and sorted_nums[mi] == sorted_nums[mi-1]:
                    mi += 1
                ri -= 1
            elif curr < 0:
                mi += 1
            else:
                ri -= 1

    return triplets
