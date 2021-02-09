class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head_node = ListNode(-1)
        head_node.next = head
        ptr0 = head_node
        ptr1 = head_node
        for i in range(n):
            ptr0 = ptr0.next
        while ptr0.next != None:
            ptr0 = ptr0.next
            ptr1 = ptr1.next
        ptr1.next = ptr1.next.next
        return head_node.next