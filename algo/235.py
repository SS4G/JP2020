# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.traverse(root, p, q)

    def traverse(self, root, p, q):
        if root is None:
            return None
        elif root.val == p.val or root.val == q.val or min(p.val, q.val) < root.val < max(p.val, q.val):
            return root
        elif root.val < p.val and root.val < q.val:
            return self.traverse(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.traverse(root.left, p, q)
        else:   
            return None