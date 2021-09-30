#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#
# https://leetcode-cn.com/problems/linked-list-random-node/description/
#
# algorithms
# Medium (62.82%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    15.7K
# Total Submissions: 24.9K
# Testcase Example:  '["Solution","getRandom","getRandom","getRandom","getRandom","getRandom"]\n' +
'[[[1,2,3]],[],[],[],[],[]]'
#
# 给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。
#
# 进阶:
# 如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？
#
# 示例:
#
#
# // 初始化一个单链表 [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
#
# // getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
# solution.getRandom();
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.d = []
        while head != None:
            self.d.append(head)
            head = head.next

        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """

    def getRandom(self) -> int:
        import random
        return self.d[random.randint(0, len(self.d)-1)].val
        """
        Returns a random node's value.
        """


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
