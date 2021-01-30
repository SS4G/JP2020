# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        else:
            paths = []
            path_stack = []
            self.helper(root, paths, path_stack)
            return path_stack

    def helper(self, root, paths, path_stack):
        if root is None:
            return
        elif root.left is None and root.right is None:
            path_stack.append(str(root.val))
            paths.append("->".join(path_stack))
            path_stack.pop()
        else:
            path_stack.append(str(root.val))
            self.helper(root.left, paths, path_stack)
            self.helper(root.right, paths, path_stack)
            path_stack.pop()
        return

