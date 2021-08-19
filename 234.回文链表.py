#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        node = head
        while node != None:
            l.append(node.val)
            node = node.next

        for n in range(len(l) // 2):
            if l[n] != l[-1 - n]:
                return False
        return True

        # @lc code=end
