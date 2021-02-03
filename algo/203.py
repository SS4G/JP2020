class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head_node = ListNode()
        rd_ptr = head
        wr_ptr = head_node
        while rd_ptr is not None:
            if rd_ptr.val != val:
                wr_ptr.next = rd_ptr
                wr_ptr = wr_ptr.next
            rd_ptr = rd_ptr.next
        if wr_ptr.next is not None:
            wr_ptr.next = None
        return head_node.next
