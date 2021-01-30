# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rows = []
        fifo = []
        rd = 0
        fifo.append((root, 0))
        while rd < len(fifo):
            node, level = fifo[rd]
            if node.left is not None:
                fifo.append((node.left, level + 1))
            if node.right is not None:
                fifo.append((node.right, level + 1))
            rd += 1
        for node, level in fifo:
            if level > len(rows) - 1:
                rows.append([])
            rows[level].append(node.val)
        rows.reverse()
        return rows
                
        

        