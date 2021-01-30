# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        minDepth = [1e9]
        self.minDepthHelper(root, 0, minDepth)
        return minDepth[0]

    def minDepthHelper(self, root, accDepth, minDepth):
        if root is None:
            return
        elif root.left is None and root.right is None:
            minDepth[0] = min(minDepth[0], accDepth + 1)
        else:
            if minDepth[0] <= accDepth:
                return 
            self.minDepthHelper(root.left, accDepth + 1, minDepth)
            self.minDepthHelper(root.right, accDepth + 1, minDepth)
