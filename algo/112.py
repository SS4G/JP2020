# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.helper(root, 0, targetSum)
    
    def helper(self, root, accSum, targetSum):
        if root is None:
            return False
        elif root.left is None and root.right is None:
            return (accSum + root.val) == targetSum
        else:
            return self.helper(root.left, accSum + root.val, targetSum) or self.helper(root.right, accSum + root.val, targetSum)
