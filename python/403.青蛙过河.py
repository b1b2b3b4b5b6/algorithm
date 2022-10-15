'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-14 11:28:06
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-14 11:58:36
FilePath: /leetcode/python/403.青蛙过河.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#
# https://leetcode.cn/problems/frog-jump/description/
#
# algorithms
# Hard (45.82%)
# Likes:    455
# Dislikes: 0
# Total Accepted:    56.8K
# Total Submissions: 123.9K
# Testcase Example:  '[0,1,3,5,6,8,12,17]'
#
# 一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。
#
# 给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。开始时，
# 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃 1 个单位（即只能从单元格 1 跳至单元格 2 ）。
#
# 如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。
# 另请注意，青蛙只能向前方（终点的方向）跳跃。
#
#
#
# 示例 1：
#
#
# 输入：stones = [0,1,3,5,6,8,12,17]
# 输出：true
# 解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子,
# 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。
#
# 示例 2：
#
#
# 输入：stones = [0,1,2,3,4,8,9,11]
# 输出：false
# 解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
#
#
#
# 提示：
#
#
# 2 <= stones.length <= 2000
# 0 <= stones[i] <= 2^31 - 1
# stones[0] == 0
# stones 按严格升序排列
#
#
#

# @lc code=start

'''
关键字
动态规划
'''




from functools import lru_cache
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        mem = {}

        def dp(now, k):
            if now == len(stones) - 1:
                return True
            if (now, k) in mem:
                return mem[(now, k)]
            left = stones[now+1:]

            def test(temp):
                if temp <= 0:
                    return False

                if stones[now] + temp not in left:
                    return False
                else:
                    return dp(stones.index(stones[now] + temp), temp)

            if now == 0:
                return test(1)

            if test(k+1) == True or test(k) == True or test(k-1) == True:
                mem[(now, k)] = True
                return True

            mem[(now, k)] = False
            return False
        return dp(0, 0)
        # @lc code=end
