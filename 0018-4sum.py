# Time complexity: O(n^2)
# Space complexity: O(n^2)
def four_sum(nums: list, target: int) -> list:
    quadruplets = set()

    sorted_nums = sorted(nums)
    pairs = dict()
    for i in range(len(sorted_nums)):
        one = sorted_nums[i]
        for j in range(i+1, len(sorted_nums)):
            two = sorted_nums[j]
            diff = target-(one+two)
            if diff in pairs:
                for three, four in pairs[diff]:
                    quadruplets.add((one, two, three, four))

        for k in range(i):
            pair = one+sorted_nums[k]
            if pair not in pairs:
                pairs[pair] = set()
            pairs[pair].add((one, sorted_nums[k]))

    return [[q[0], q[1], q[2], q[3]] for q in quadruplets]
