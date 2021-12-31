# Time complexity: O(n)
# Space complexity: O(n)
def max_ancestor_diff(root) -> int:
    def dfs(node):
        if not node: return float('inf'), float('-inf'), 0
        left = dfs(node.left)
        right = dfs(node.right)
        new_min = min(left[0], right[0], node.val)
        new_max = max(left[1], right[1], node.val)
        return new_min, new_max, max(left[2], right[2], abs(node.val-new_min), abs(node.val-new_max))

    res = dfs(root)
    return res[2]
