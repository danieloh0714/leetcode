# Time complexity: O(n)
# Space complexity: O(n)
def build_tree(preorder: list, inorder: list):
    preorder_copy = preorder.copy()
    inorder_idxs = {val: i for i, val in enumerate(inorder)}

    def recurse(li, ri):
        if li > ri: return None
        node = TreeNode(preorder_copy.pop(0))
        mi = inorder_idxs[node.val]
        node.left = recurse(li, mi-1)
        node.right = recurse(mi+1, ri)
        return node

    return recurse(0, len(inorder)-1)
