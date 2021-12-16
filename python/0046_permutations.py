def permute(nums: list) -> list:
    if not nums: return []

    permutations = []

    def recurse(nums_left, permutation):
        if not nums_left:
            permutations.append(permutation)
        else:
            for i, n in enumerate(nums_left):
                recurse(nums_left[:i]+nums_left[i+1:], permutation+[n])

    recurse(nums, [])
    return permutations
