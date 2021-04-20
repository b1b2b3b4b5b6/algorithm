'''
Author: your name
Date: 2021-01-14 07:11:53
LastEditTime: 2021-01-14 07:41:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/141.环形链表.py
'''
#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head

        while True:
            if fast == None or fast.next == None:
                return False

            slow = slow.next

            fast = fast.next.next

            if fast == slow:
                return True
            # @lc code=end
