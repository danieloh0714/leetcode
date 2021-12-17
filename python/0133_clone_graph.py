# Time complexity: O(n)
# Space complexity: O(n)
def clone_graph(node):
    if not node: return None

    nodes = dict()

    def dfs(n):
        if n.val in nodes: return nodes[n.val]

        nodes[n.val] = Node(n.val)
        new_node = nodes[n.val]

        for neighbor in n.neighbors:
            new_node.neighbors.append(dfs(neighbor))

        return new_node

    return dfs(node)
