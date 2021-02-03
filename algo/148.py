# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def showLinkedList(head, head_node=False):
    res = []
    if head_node:
        head = head.next
    while head is not None:
        res.append(str(head.val))
        head = head.next
    #print(res)
    print("->".join(res))

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        return self.sortHelper(head)

    def sortHelper(self, head):
        if head is None or head.next is None:
            return head
        fast = head
        slow = head
        while fast is not None:
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
            if fast is None:
                break
            slow = slow.next
        left_head = head
        right_head = slow.next
        slow.next = None
        #print("left={} right={}".format(left_head.val, right_head.val))
        left_part = self.sortHelper(left_head)
        right_part = self.sortHelper(right_head)
        #print("left_part={} right_part={}".format(left_part.val, right_part.val))
        #showLinkedList(left_part)
        #showLinkedList(right_part)
        merged_res = self.mergeSort(left_part, right_part)
        #showLinkedList(merged_res)
        return merged_res

    def mergeSort(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left

        head_node = ListNode(-1)
        tmp = head_node
        while left is not None and right is not None:
            if left.val < right.val:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next
            tmp = tmp.next

        notNonePtr = left if left is not None else right
        tmp.next = notNonePtr
        return head_node.next



if __name__ == "__main__":
    arr = [3, 4, 1]
    head = ListNode()
    tmp = head
    for a in arr:
        tmp.next = ListNode(a)
        tmp = tmp.next
        print(tmp.val)
    #showLinkedList(head.next)
    s = Solution()
    showLinkedList(s.sortList(head.next))
    #showLinkedList(head)






        