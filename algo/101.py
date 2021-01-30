# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.symmetricHelper(root.left, root.right)
        
    def symmetricHelper(self, leftRoot, rightRoot):
        if leftRoot is None and rightRoot is None:
            return True
        elif leftRoot is None or rightRoot is None:
            return False
        elif leftRoot.val == rightRoot.val:
            return self.symmetricHelper(leftRoot.right, rightRoot.left) and self.symmetricHelper(leftRoot.left, rightRoot.right)
        else:
            return False
        

