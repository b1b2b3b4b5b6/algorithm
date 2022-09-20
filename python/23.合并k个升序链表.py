'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-01 16:37:31
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-02 10:58:24
FilePath: /leetcode/python/23.合并k个升序链表.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (57.24%)
# Likes:    2146
# Dislikes: 0
# Total Accepted:    535.3K
# Total Submissions: 934.9K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
#
# 示例 2：
#
# 输入：lists = []
# 输出：[]
#
#
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]
#
#
#
#
# 提示：
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        out = None
        temp = None
        while True:
            m = -1
            for n in range(len(lists)):
                if lists[n] == None:
                    continue

                if m == -1 or lists[n].val <= lists[m].val:
                    m = n

            if m == -1:
                break

            if out == None:
                out = lists[m]
                temp = out
            else:
                out.next = lists[m]
                out = lists[m]

            lists[m] = lists[m].next

        return temp
        # @lc code=end
