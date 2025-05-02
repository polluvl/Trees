# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            parent = root
            temp = root.right
            while temp.left:
                parent = temp
                temp = temp.left
            
            root.val = temp.val
            if parent!= root:
                parent.left = self.deleteNode(parent.left, temp.val)
            else:
                parent.right = self.deleteNode(parent.right, temp.val)

        return root
