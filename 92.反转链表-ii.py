# @before-stub-for-debug-begin
from python3problem92 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: your name
Date: 2021-01-07 01:01:56
LastEditTime: 2021-01-08 08:16:54
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/92.反转链表-ii.py
'''
#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        offset = 0

        if head == None:
            return None

        now_node = head
        last_node = None
        pre_node = None
        start_node = None
        stop_node = None
        after_node = None
        offset = 0
        while True:
            offset += 1
            next_node = now_node.next
            if offset > m and offset <= n:
                now_node.next = last_node

            if offset == m:
                pre_node = last_node
                start_node = now_node
            if offset == n:
                stop_node = now_node
                after_node = next_node
                break

            last_node = now_node
            now_node = next_node

        if m == 1:
            head = stop_node
        else:
            pre_node.next = stop_node

        start_node.next = after_node

        return head

        # @lc code=end
