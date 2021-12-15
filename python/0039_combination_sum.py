# Time complexity: O(2^target)
def combination_sum(candidates: list, target: int) -> list:
    combos = []

    def recurse(i, combo, total):
        if total == target:
            combos.append(combo.copy())
        elif i < len(candidates) and total < target:
            candidate = candidates[i]
            recurse(i+1, combo, total)
            combo.append(candidate)
            recurse(i, combo, total+candidate)
            combo.pop()

    recurse(0, [], 0)
    return combos
