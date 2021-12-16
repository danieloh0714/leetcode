# Time complexity: O(n)
# Space complexity: O(h)
def max_depth(root) -> int:
    if not root: return 0

    depth = 1
    for child in root.children:
        depth = max(depth, max_depth(child)+1)

    return depth
