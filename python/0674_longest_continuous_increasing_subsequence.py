def find_length_of_LIS(nums: list) -> int:
    ans = 1
    curr = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            curr += 1
        else:
            ans = max(ans, curr)
            curr = 1

    return max(ans, curr)
