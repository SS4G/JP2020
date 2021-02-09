# Definition for singly-linked list.
from utils import ListNode, LinkedListUtil

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head_node1 = ListNode()
        head_node1.next = head
        slow = head_node1
        fast = head_node1
        while fast is not None:
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
            slow = slow.next
        head_node2 = ListNode()
        head_node2.next = slow.next
        slow.next = None

        #LinkedListUtil.showList(head_node1)
        #LinkedListUtil.showList(head_node2)

        rev_head_node = ListNode()
        rev_ptr = head_node2.next
        while rev_ptr is not None:
            last_next_node = rev_head_node.next
            rev_head_node.next = rev_ptr
            rev_ptr = rev_ptr.next
            rev_head_node.next.next = last_next_node
        
        merged_head_node = ListNode()
        merge_ptr1 = rev_head_node.next
        merge_ptr0 = head_node1.next
        merged_ptr = merged_head_node
        turn_flag = True
        while merge_ptr0 is not None and merge_ptr1 is not None:
            if turn_flag:
                merged_ptr.next = merge_ptr0
                merge_ptr0 = merge_ptr0.next
            else:
                merged_ptr.next = merge_ptr1
                merge_ptr1 = merge_ptr1.next
            merged_ptr = merged_ptr.next
            turn_flag = not turn_flag

        if merge_ptr0 is not None:
            merged_ptr.next = merge_ptr0
            merged_ptr = merged_ptr.next
        elif merge_ptr1 is not None:
            merged_ptr.next = merge_ptr1
            merged_ptr = merged_ptr.next
        return merged_head_node
        #not_none_ptr = merge_ptr0 if merge_ptr0 is not None else merge_ptr1

if __name__ == "__main__":
    s = Solution()
    l1 = LinkedListUtil.genList([1,])
    LinkedListUtil.showList(l1)
    res = s.reorderList(l1)
    LinkedListUtil.showList(res)

        

        
        