#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (49.36%)
# Likes:    1116
# Dislikes: 0
# Total Accepted:    304.3K
# Total Submissions: 615.1K
# Testcase Example:  '[1,2,2,1]'
#
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,2,1]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：head = [1,2]
# 输出：false
#
#
#
#
# 提示：
#
#
# 链表中节点数目在范围[1, 10^5] 内
# 0 <= Node.val <= 9
#
#
#
#
# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
快慢指针可以实现O(1)空间复杂度
'''


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
