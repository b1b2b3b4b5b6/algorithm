'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-01 15:48:07
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-01 16:03:05
FilePath: /leetcode/python/2.两数相加.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode.cn/problems/add-two-numbers/description/
#
# algorithms
# Medium (42.08%)
# Likes:    8575
# Dislikes: 0
# Total Accepted:    1.5M
# Total Submissions: 3.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
# 示例 1：
#
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
#
# 示例 2：
#
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
# 示例 3：
#
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#
#
#
# 提示：
#
#
# 每个链表中的节点数在范围 [1, 100] 内
# 0
# 题目数据保证列表表示的数字不含前导零
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
关键字
遍历
'''


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = l1
        right = l2
        out = None
        ret = None
        up = 0
        while True:
            if left is None and right is None:
                break

            if left is not None:
                left_val = left.val
                left = left.next
            else:
                left_val = 0

            if right is not None:
                right_val = right.val
                right = right.next
            else:
                right_val = 0

            val = left_val + right_val + up
            up = val // 10
            if out is None:
                out = ListNode(val % 10)
                ret = out
            else:
                out.next = ListNode(val % 10)
                out = out.next
        if up != 0:
            out.next = ListNode(up)
        return ret
        # @lc code=end
