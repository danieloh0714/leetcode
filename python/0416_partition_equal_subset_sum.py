def can_partition(nums: list) -> bool:
    total = sum(nums)
    if total%2 != 0: return False
    target = total/2

    s = set([0])
    for n in nums:
        new_s = set()
        for el in s:
            if el+n == target: return True
            new_s.add(el)
            new_s.add(el+n)
        s = new_s

    return False
