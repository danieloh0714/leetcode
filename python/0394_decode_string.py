# Time complexity: O(n)
# Space complexity: O(1)
def decode_string(s: str) -> str:
    stack = []

    for char in s:
        if char != ']':
            stack.append(char)
        else:
            substr = []
            while stack[-1] != '[':
                substr.append(stack.pop())
            stack.pop()
            substr = ''.join(substr[::-1])

            k = []
            while stack and stack[-1].isdigit():
                k.append(stack.pop())
            k = int(''.join(k[::-1]))

            for _ in range(k):
                stack.append(substr)

    return ''.join(stack)
