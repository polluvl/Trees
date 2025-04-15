# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    if not isinstance(node, Node):
        raise ValueError
    outp = []
    temp = node
    outp.append(node.data)
    if temp.left or temp.right:
        if temp.left:
            outp.extend(pre_order(temp.left))
        if temp.right:
            outp.extend(pre_order(temp.right))
    return outp

# In-order traversal
def in_order(node):
    if node is None:
        return []
    if not isinstance(node, Node):
        raise ValueError
    outp = []

    if node.left:
        outp.extend(in_order(node.left))
    
    outp.append(node.data)
    
    if node.right:
        outp.extend(in_order(node.right))
    return outp

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    if not isinstance(node, Node):
        raise ValueError
    outp = []
    temp = node
    if temp.right or temp.left:
        if temp.left:
            outp.extend(post_order(temp.left))
        if temp.right:
            outp.extend(post_order(temp.right))
    outp.append(node.data)
        
    return outp
