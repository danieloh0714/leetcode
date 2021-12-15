# Time complexity: O(n)
# Space complexity: O(n)
def is_valid(s: str) -> bool:
    stack = []

    mappings = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in mappings:
            if not stack or stack.pop() != mappings[char]:
                return False

    return not stack
