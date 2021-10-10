#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
# https://leetcode-cn.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (45.13%)
# Likes:    582
# Dislikes: 0
# Total Accepted:    69.3K
# Total Submissions: 153.1K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
#
# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
#
# 注意：不允许旋转信封。
#
#
# 示例 1：
#
#
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
#
# 示例 2：
#
#
# 输入：envelopes = [[1,1],[1,1],[1,1]]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1
# envelopes[i].length == 2
# 1 i, hi
#
#
#

# @lc code=start

'''
关键字
区间调度 动态规划

转换成求最长递增子序列长度：
    按宽递增排序，找长的最长子序列长

细节问题：
    对于宽相等的情况，由于只能取一个，故对于宽相等的长进行递减排序
    
'''


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        import functools

        def my_compare(l1, l2):
            if l1[0] > l2[0]:
                return 1

            if l1[0] < l2[0]:
                return -1

            if l1[1] > l2[1]:
                return -1

            if l1[1] < l2[1]:
                return 1

            return 0
        envelopes.sort(key=functools.cmp_to_key(my_compare))

        target = [x[1] for x in envelopes]

        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]

            res = 1
            for i in range(n+1, len(target)):
                if target[i] > target[n]:
                    res = max(res, dp(i) + 1)

            memo[n] = res
            return memo[n]

        for n in range(len(target)):
            dp(n)

        return max(memo.values())
        # @lc code=end
