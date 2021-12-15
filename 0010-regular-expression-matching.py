# Time complexity: O(mn)
# Space complexity: O(mn)
def is_match(s: str, p: str) -> bool:
    cache = {}

    def recurse(si, pi):
        if si == len(s) and pi == len(p): return True
        if pi == len(p): return False
        if (si, pi) in cache: return cache[(si, pi)]

        is_match = si < len(s) and (p[pi] == '.' or s[si] == p[pi])
        if pi < len(p)-1 and p[pi+1] == '*':
            cache[(si, pi)] = recurse(si, pi+2) or (is_match and recurse(si+1, pi))
            return cache[(si, pi)]
        if is_match:
            cache[(si, pi)] = recurse(si+1, pi+1)
            return cache[(si, pi)]

        cache[(si, pi)] = False
        return False

    return recurse(0, 0)
