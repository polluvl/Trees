# Pre-order traversal
def pre_order(node):
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
    return []

# Post-order traversal
def post_order(node):
    return []

