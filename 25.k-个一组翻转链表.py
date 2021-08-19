#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def turn_item(start, end) -> ListNode:

            next = start.next
            if next == None:
                return start

            if start == end:
                return start

            t_head = turn_item(start.next, end)

            next.next = start
            start.next = None
            return t_head

        temp_start = head
        res = head
        while True:
            i = 1
            now = temp_start
            if now == None:
                return res
            while i < k:

                now = now.next
                if now == None:
                    return res
                i += 1

            start = temp_start
            end = now
            temp_start = now.next

            if start == head:
                res = turn_item(start, end)

            else:
                temp_end.next = turn_item(start, end)

            temp_end = start
            temp_end.next = temp_start

        # @lc code=end
