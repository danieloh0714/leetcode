# Time complexity: O(n)
# Space complexity: O(h)
def max_depth(root) -> int:
    if not root: return 0
    return max(max_depth(root.left), max_depth(root.right))+1
