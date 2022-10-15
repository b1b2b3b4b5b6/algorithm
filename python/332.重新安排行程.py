'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-08 18:45:13
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-09 15:10:17
FilePath: /leetcode/python/332.重新安排行程.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
# https://leetcode.cn/problems/reconstruct-itinerary/description/
#
# algorithms
# Hard (47.08%)
# Likes:    648
# Dislikes: 0
# Total Accepted:    69.1K
# Total Submissions: 146.7K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# 给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi]
# 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。
#
# 所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK
# 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。
#
#
# 例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。
#
#
# 假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。
#
#
#
# 示例 1：
#
#
# 输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# 输出：["JFK","MUC","LHR","SFO","SJC"]
#
#
# 示例 2：
#
#
# 输入：tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
# 解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。
#
#
#
#
# 提示：
#
#
# 1
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi 和 toi 由大写英文字母组成
# fromi != toi
#
#
#

# @lc code=start

'''
关键字
回溯 贪心
'''


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        lines = []
        for l in tickets:
            f = l[0]
            t = l[1]
            lines.append(f'{f}>{t}')
            if f not in graph:
                graph[f] = []
            graph[f].append(t)
            graph[f].sort()

        def dp(path, left):
            if len(left) == 0:
                return True
            now = path[-1]

            if now not in graph:
                return False

            for to in graph[now]:
                line = f'{now}>{to}'
                if line not in left:
                    continue
                path.append(to)
                left.remove(line)
                if dp(path, left) == True:
                    return True
                path.pop()
                left.append(line)

            return False

        p = ['JFK']
        dp(p, lines)
        return p
        # @lc code=end
