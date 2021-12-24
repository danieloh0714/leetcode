# Time complexity: O(n)
# Space complexity: O(h)
def rob(root) -> int:
    def dfs(node) -> tuple:
        if not node: return 0, 0

        left, right = dfs(node.left), dfs(node.right)

        without_node = left[0] + right[0]
        with_node = max(node.val + left[1] + right[1], without_node)

        return with_node, without_node

    return max(dfs(root))
