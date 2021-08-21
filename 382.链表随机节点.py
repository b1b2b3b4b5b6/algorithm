#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.m = {}
        len = 0
        node = head
        while node != None:
            self.m[len] = node
            len += 1
            node = node.next

    def getRandom(self) -> int:
        l = len(self.m)
        import random
        r = random.randint(0, l-1)
        return self.m[r].val
        """
        Returns a random node's value.
        """


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
