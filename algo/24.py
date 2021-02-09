# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#from typing import List
from utils import ListNode
from utils import LinkedListUtil as lu

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_node = ListNode(-1)
        head_node.next = head
        next_head = head_node
        while True:
            next_head = self.swapNext2(next_head)
            #print(next_head.val)
            if next_head is None:
                break
        return head_node.next

    def swapNext2(self, head):
        if head is None:
            return None
        next1 = head.next
        if next1 is None:
            return None
        next2 = head.next.next
        if next2 is None:
            return None

        head.next = next2
        next1.next = next2.next
        next2.next = next1
        return next1

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    array = []
    head = lu.genList(array)
    lu.showList(head)
    s = Solution()
    res = s.swapPairs(head)
    lu.showList(res)
