# Time complexity: O(n)
# Space complexity: O(h)
def flatten(root) -> None:
    def recurse(node):
        if not node: return None

        left_tail = recurse(node.left)
        right_tail = recurse(node.right)

        if node.left:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        return right_tail or left_tail or node

    recurse(root)
