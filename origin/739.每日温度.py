#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
# https://leetcode-cn.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (67.96%)
# Likes:    884
# Dislikes: 0
# Total Accepted:    211.1K
# Total Submissions: 310.6K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 请根据每日 气温 列表 temperatures ，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#
# 示例 1:
#
#
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
#
#
# 示例 2:
#
#
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
#
#
# 示例 3:
#
#
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]
#
#
#
# 提示：
#
#
# 1
# 30
#
#
#

# @lc code=start

'''
关键字
单调栈

下一个更大值:单调栈
'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for n in range(len(temperatures)-1, -1, -1):
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[n]:
                stack.pop(-1)

            if len(stack) == 0:
                res.append(0)
            else:
                res.append(stack[-1] - n)
            stack.append(n)

        res.reverse()
        return res
        # @lc code=end
