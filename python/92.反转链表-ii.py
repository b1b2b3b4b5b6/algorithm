#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (54.74%)
# Likes:    1014
# Dislikes: 0
# Total Accepted:    203.2K
# Total Submissions: 371.2K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
# 反转后的链表 。
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
#
# 示例 2：
#
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
#
#
# 提示：
#
#
# 链表中节点数目为 n
# 1
# -500
# 1
#
#
#
#
# 进阶： 你可以使用一趟扫描完成反转吗？
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
递归
'''


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        if head == None:
            return head
        if left == right:
            return head

        def reverse(last_node, now_node, offset):

            next_node = now_node.next
            now_node.next = last_node
            if offset == right:
                return now_node, next_node
            else:
                return reverse(now_node, next_node, offset+1)

        n = 1
        node = head
        last_node = None
        while True:
            if n == left:
                res = reverse(None, node, n)
                if last_node == None:
                    head = res[0]
                else:
                    last_node.next = res[0]
                node.next = res[1]
                break
            n += 1
            last_node = node
            node = node.next

        return head
        # @lc code=end
