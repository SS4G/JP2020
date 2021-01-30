# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptra = headA
        ptrb = headB
        while ptra is not None and ptrb is not None:
            if ptra == ptrb:
                return ptrb
            ptra = ptra.next
            ptrb = ptrb.next
        if ptra is None and ptrb is None:
            return None

        diff = 0
        notNonePtr = ptrb if ptra is None else ptra
        headAIsShort = True if ptra is None else False

        while notNonePtr is not None:
            notNonePtr = notNonePtr.next
            diff += 1

        ptra = headA
        ptrb = headB
        for i in range(diff):
            if headAIsShort:
                ptrb = ptrb.next
            else:
                ptra = ptra.next
        
        while ptra is not None and ptrb is not None:
            if ptra == ptrb:
                return ptrb
            ptra = ptra.next
            ptrb = ptrb.next
        if ptra is None and ptrb is None:
            return None

        return None