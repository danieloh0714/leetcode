# Time complexity: O(nlog(m))
# Space complexity: O(n)
def group_anagrams(strs: list) -> list:
    anagrams = dict()

    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = []
        anagrams[sorted_s].append(s)

    return list(anagrams.values())
