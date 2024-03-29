#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#
# https://leetcode.cn/problems/ipo/description/
#
# algorithms
# Hard (44.96%)
# Likes:    275
# Dislikes: 0
# Total Accepted:    37.7K
# Total Submissions: 83.8K
# Testcase Example:  '2\n0\n[1,2,3]\n[0,1,1]'
#
# 假设 力扣（LeetCode）即将开始 IPO 。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。
# 由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。
# 
# 给你 n 个项目。对于每个项目 i ，它都有一个纯利润 profits[i] ，和启动该项目需要的最小资本 capital[i] 。
# 
# 最初，你的资本为 w 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。
# 
# 总而言之，从给定项目中选择 最多 k 个不同项目的列表，以 最大化最终资本 ，并输出最终可获得的最多资本。
# 
# 答案保证在 32 位有符号整数范围内。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# 输出：4
# 解释：
# 由于你的初始资本为 0，你仅可以从 0 号项目开始。
# 在完成后，你将获得 1 的利润，你的总资本将变为 1。
# 此时你可以选择开始 1 号或 2 号项目。
# 由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
# 因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。
# 
# 
# 示例 2：
# 
# 
# 输入：k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# 输出：6
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= k <= 10^5
# 0 <= w <= 10^9
# n == profits.length
# n == capital.length
# 1 <= n <= 10^5
# 0 <= profits[i] <= 10^4
# 0 <= capital[i] <= 10^9
# 
# 
#

# @lc code=start

'''
关键字
贪心法

总是选择成本足够情况下，利润最大的项目进行
故建立有序数组，按照利润排序，按照成本依次加入
'''




from sortedcontainers import SortedList
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        sl = SortedList(key=lambda m: profits[m])
        cap_sl = SortedList([i for i in range(len(capital))],
                            key=lambda m: capital[m])
        while True:
            while len(cap_sl) > 0 and capital[cap_sl[0]] <= w:
                sl.add(cap_sl.pop(0))
            if len(sl) == 0:
                break

            w += profits[sl[-1]]
            sl.pop(-1)
            k -= 1
            if k == 0:
                break
        return w
# @lc code=end

