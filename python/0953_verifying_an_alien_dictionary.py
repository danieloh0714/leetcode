# Time complexity: O(m)
# Space complexity: O(1)
def is_alien_sorted(words: list, order: str) -> bool:
    letter_pos = {letter: i for i, letter in enumerate(order)}

    def in_order(prev: str, curr: str) -> bool:
        pi, ci = 0, 0
        while pi < len(prev) and ci < len(curr):
            p, c = prev[pi], curr[ci]
            if letter_pos[p] < letter_pos[c]: return True
            if letter_pos[p] > letter_pos[c]: return False
            pi += 1
            ci += 1

        return pi == len(prev)

    for i in range(1, len(words)):
        if not in_order(words[i-1], words[i]):
            return False

    return True
