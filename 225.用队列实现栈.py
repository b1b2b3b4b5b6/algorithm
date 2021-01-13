'''
Author: your name
Date: 2021-01-08 09:00:00
LastEditTime: 2021-01-12 03:26:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/225.用队列实现栈.py
'''
#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start


class MyStack:
    a = []
    b = []
    flag = 'a'

    def __init__(self):
        self.a = []
        self.b = []
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        if self.flag == 'a':
            self.a.append(x)
        else:
            self.b.append(x)
        """
        Push element x onto stack.
        """

    def pop(self) -> int:
        if self.flag == 'a':
            self.b.clear()
            while len(self.a) > 1:
                self.b.append(self.a.pop(0))
            self.flag = 'b'
            return self.a.pop(0)
        else:
            self.a.clear()
            while len(self.b) > 1:
                self.a.append(self.b.pop(0))
            self.flag = 'a'
            return self.b.pop(0)

        """
        Removes the element on top of the stack and returns that element.
        """

    def top(self) -> int:
        if self.flag == 'a':
            self.b.clear()
            while len(self.a) > 1:
                self.b.append(self.a.pop(0))
            self.flag = 'b'
            val = self.a.pop(0)
            self.b.append(val)
            return val
        else:
            self.a.clear()
            while len(self.b) > 1:
                self.a.append(self.b.pop(0))
            self.flag = 'a'
            val = self.b.pop(0)
            self.a.append(val)
            return val
        """
        Get the top element.
        """

    def empty(self) -> bool:
        if len(self.a) + len(self.b) > 0:
            return False
        else:
            return True

        """
        Returns whether the stack is empty.
        """


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
