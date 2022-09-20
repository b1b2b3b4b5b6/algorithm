'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-08-31 10:39:48
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-08-31 11:29:13
FilePath: /leetcode/python/116.填充每个节点的下一个右侧节点指针.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#
# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (71.94%)
# Likes:    861
# Dislikes: 0
# Total Accepted:    287.4K
# Total Submissions: 399.5K
# Testcase Example:  '[1,2,3,4,5,6,7]'
#
# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
#
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
#
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
#
#
# 示例 1：
#
#
#
#
# 输入：root = [1,2,3,4,5,6,7]
# 输出：[1,#,2,3,#,4,5,6,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由
# next 指针连接，'#' 标志着每一层的结束。
#
#
#
#
# 示例 2:
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中节点的数量在 [0, 2^12 - 1] 范围内
# -1000 <= node.val <= 1000
#
#
#
#
# 进阶：
#
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
#
#
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

'''
关键字
BFS
'''


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = []
        if root is not None:
            q.append(root)

        while len(q) > 0:
            if len(q) > 1:
                for n in range(len(q) - 1):
                    q[n].next = q[n+1]

            next_q = []
            for node in q:
                if node.left is not None:
                    next_q.append(node.left)
                if node.right is not None:
                    next_q.append(node.right)
            q = next_q
        return root
        # @lc code=end
