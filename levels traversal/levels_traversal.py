def tree_by_levels(node):
    visited = []
    queue = []
    if node is None:
        return []
    if not isinstance(node, Node):
        raise ValueError
    visited.append(node.value)
    queue.append(node)
    while queue:
        temp = queue.pop(0)
        if temp.left:
            queue.append(temp.left)
            visited.append(temp.left.value)
        if temp.right:
            queue.append(temp.right)
            visited.append(temp.right.value)
    return visited
