# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from utils import ListNode
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head_node = ListNode(0)
        head_node.next = head

    def reverseK(head_node, k):
        dummpy_node = ListNode(0)
        dummpy_node.next = head_node
        tmp_ptr = dummpy_node
        for i in range(k):
            tmp_ptr = tmp_ptr.next
            if i < k - 1 and tmp_ptr is None:
                return dummpy_node.next
            

