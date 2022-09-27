#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
# https://leetcode.cn/problems/candy/description/
#
# algorithms
# Hard (49.53%)
# Likes:    994
# Dislikes: 0
# Total Accepted:    173.7K
# Total Submissions: 350.7K
# Testcase Example:  '[1,0,2]'
#
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
#
# 你需要按照以下要求，给这些孩子分发糖果：
#
#
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
#
#
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
#
#
#
# 示例 1：
#
#
# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
#
#
# 示例 2：
#
#
# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
# ⁠    第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
#
#
#
# 提示：
#
#
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4
#
#
#

# @lc code=start
'''
关键字
技巧

'''


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1

        right = ret = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)

        return ret

        # @lc code=end
        # out = [max(ratings) + 2]
        # ratings.insert(0, max(ratings) + 1)

        # def dp(n):

        #     if n == len(ratings):
        #         return True

        #     now = ratings[n]
        #     last = ratings[n-1]
        #     if now == last:
        #         i = 1
        #         while True:
        #             out.append(i)
        #             if dp(n + 1) == False:
        #                 out.pop()
        #                 i += 1
        #             else:
        #                 return True

        #     elif now > last:
        #         i = out[-1] + 1
        #         while True:
        #             out.append(i)
        #             if dp(n + 1) == False:
        #                 out.pop()
        #                 i += 1
        #             else:
        #                 return True

        #     elif now < last:
        #         for i in range(1, out[-1]):
        #             out.append(i)
        #             if dp(n + 1) == False:
        #                 out.pop()
        #                 i += 1
        #             else:
        #                 return True
        #         return False

        # dp(1)
        # out.pop(0)
        # print(out)
        # return sum(out)
