#
# @lc app=leetcode.cn id=261 lang=python3
#
# [261] 以图判树
#
# https://leetcode-cn.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (49.70%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    8.3K
# Total Submissions: 16.8K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# 给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。
#
# 示例 1：
#
# 输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
# 输出: true
#
# 示例 2:
#
# 输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# 输出: false
#
# 注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表
# edges 中。
#
#

# @lc code=start

'''
有效树：
    节点数要全
    只有一个根节点
    不能闭环
'''


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 1:
            return True

        node_dict = {}

        def find_root(x):
            while node_dict[x] != x:
                x = node_dict[x]
            return x

        for l in edges:
            left = l[0]
            right = l[1]

            if left not in node_dict:
                node_dict[left] = left

            if right not in node_dict:
                node_dict[right] = right

            if find_root(left) == find_root(right):
                return False

            node_dict[find_root(right)] = find_root(left)

        count = 0

        for k, v in node_dict.items():
            if k == v:
                count += 1

        if count != 1:
            return False

        if len(node_dict.keys()) < n:
            return False

        return True
        # @lc code=end
