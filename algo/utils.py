class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None


class LinkedListUtil:
    @staticmethod
    def merge2Ascendinglist(l1, l2):
        """
        合并两个升序的链表
        合并后仍然是一个升序的链表
        :param l1:
        :param l2:
        :return:
        """
        t1 = l1
        t2 = l2
        newHead = None
        tmp = None
        while (t1 is not None) and (t2 is not None):
            if newHead is None:
                if t1.val < t2.val:
                    newHead = t1
                    t1 = t1.next
                else:
                    newHead = t2
                    t2 = t2.next
                tmp = newHead
            else:
                if t1.val < t2.val:
                    tmp.next = t1
                    t1 = t1.next
                else:
                    tmp.next = t2
                    t2 = t2.next
                tmp = tmp.next
        if t1 is not None:
            tmp.next = t1
        if t2 is not None:
            tmp.next = t2
        return newHead

    @staticmethod
    def size(head):
        cnt = 0
        while head is not None:
            head = head.next
            cnt += 1
        return cnt

    @staticmethod
    def toPosition(head, pos):
        while pos > 0:
            head = head.next
            pos -= 1
        return head

    @staticmethod
    def link2Arr(head, length=-1):
        output = []
        if length == -1:
            while head is not None:
                output.append(head.val)
                head = head.next
        else:
            l = 0
            while head is not None:
                output.append(head.val)
                l += 1
                if l == length:
                    break
                head = head.next
        # print(output)
        return output

    @staticmethod
    def showList(head, length=-1):
        if length == -1:
            print("->".join([str(int0) for int0 in LinkedListUtil.link2Arr(head)]))
        else:
            print("->".join([str(int0) for int0 in LinkedListUtil.link2Arr(head, length=length)]))

    @staticmethod
    def genList(l):
        head = None
        tmp = head
        for val in l:
            if head is None:
                head = ListNode(val)
                tmp = head
            else:
                tmp.next = ListNode(val)
                tmp = tmp.next
        return head
