'''
Author: your name
Date: 2021-01-08 08:18:26
LastEditTime: 2021-01-08 08:59:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/232.用栈实现队列.py
'''
#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start


class MyQueue:
    a = []
    b = []

    def __init__(self):
        self.a = []
        self.b = []
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        self.a.append(x)
        """
        Push element x to the back of queue.
        """

    def pop(self) -> int:
        if len(self.b) == 0:
            while len(self.a) != 0:
                self.b.append(self.a.pop())
        return self.b.pop()
        """
        Removes the element from in front of queue and returns that element.
        """

    def peek(self) -> int:
        if len(self.b) == 0:
            while len(self.a) != 0:
                self.b.append(self.a.pop())
        return self.b[-1]
        """
        Get the front element.
        """

    def empty(self) -> bool:
        if len(self.a) == 0 and len(self.b) == 0:
            return True
        else:
            return False
        """
        Returns whether the queue is empty.
        """


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
