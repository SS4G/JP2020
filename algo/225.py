from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.fifo1 = deque()
        self.fifo2 = deque()
        self.fifo1_flag = True


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if self.fifo1_flag:
            self.fifo1.append(x)
        else:
            self.fifo2.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.fifo1_flag:
            while len(self.fifo1) > 1:
                self.fifo2.append(self.fifo1.popleft())
            self.fifo1_flag = False
            return self.fifo1.popleft()
        else:
            while len(self.fifo2) > 1:
                self.fifo1.append(self.fifo2.popleft())
            self.fifo1_flag = True
            return self.fifo2.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.fifo1_flag:
            while len(self.fifo1) > 1:
                self.fifo2.append(self.fifo1.popleft())
            self.fifo1_flag = False
            last = self.fifo1.popleft()
            self.fifo2.append(last)
        else:
            while len(self.fifo2) > 1:
                self.fifo1.append(self.fifo2.popleft())
            self.fifo1_flag = True
            last = self.fifo2.popleft()
            self.fifo1.append(last)
        return last

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.fifo1) == 0 and len(self.fifo2) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()