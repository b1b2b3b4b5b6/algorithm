#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (65.55%)
# Likes:    1248
# Dislikes: 0
# Total Accepted:    210.9K
# Total Submissions: 321.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 进阶：
#
#
# 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#
#
# 示例 2：
#
#
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#
#
# 示例 3：
#
#
# 输入：head = [1,2,3,4,5], k = 1
# 输出：[1,2,3,4,5]
#
#
# 示例 4：
#
#
# 输入：head = [1], k = 1
# 输出：[1]
#
#
#
#
#
# 提示：
#
#
# 列表中节点的数量在范围 sz 内
# 1
# 0
# 1
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
先写出翻转k个以链表的函数
然后每k个调用上面的函数,分段处理
'''


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        def turn(start, end):
            if start == end:
                return end
            next = turn(start.next, end)
            next.next = start
            return start

        new_head = None

        node = head
        last_end = None
        while node != None:
            n = 0
            start = node
            while node != None:
                n += 1
                end = node
                node = node.next

                if n == k:
                    turn(start, end)
                    temp = start
                    start = end
                    end = temp
                    break

            if new_head == None:
                new_head = start
                last_end = end
            else:
                last_end.next = start
                last_end = end
        last_end.next = None
        return new_head
        # @lc code=end
