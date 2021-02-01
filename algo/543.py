# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longgestPaths = [0, ]
        self.longgestPath(root, longgestPaths)
        return longgestPaths[0]

    def longgestPath(self, root, longgestPaths):
        if root is None:
            return 0
        else:
            leftPath = self.longgestPath(root.left, longgestPaths)
            rightPath = self.longgestPath(root.right, longgestPaths)
            crossRootPath = (leftPath + rightPath + 1)
            longgestPaths[0] = max(longgestPaths[0], crossRootPath)
            return max(leftPath, rightPath) + 1
