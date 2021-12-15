# Time complexity: O(4^n*n)
# Space complexity: O(4^n*n)
def letter_combinations(digits: str) -> list:
    if digits == '': return []

    mappings = { '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz' }

    combos = []
    def recurse(i, combo):
        if i == len(digits):
            combos.append(''.join(combo))
            return
        for letter in mappings[digits[i]]:
            recurse(i+1, combo+[letter])

    recurse(0, [])
    return combos
