# @before-stub-for-debug-begin
from python3problem142 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2021-01-14 07:42:01
LastEditTime: 2021-01-20 07:58:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/142.环形链表-ii.py
'''
#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        d = []
        node = head
        if head == None:
            return None

        d = [head]
        while True:
            if node == None:
                return None
            node = node.next
            if node in d:
                return node
            else:
                d.append(node)
                # @lc code=end
