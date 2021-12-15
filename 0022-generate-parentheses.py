def generate_parenthesis(n: int) -> list:
    combos = []

    combo = []
    def recurse(num_open, num_closed):
        if num_open == n and num_closed == n:
            combos.append(''.join(combo))
            return
        if num_open < n:
            combo.append('(')
            recurse(num_open+1, num_closed)
            combo.pop()
        if num_closed < num_open:
            combo.append(')')
            recurse(num_open, num_closed+1)
            combo.pop()

    recurse(0, 0)
    return combos
