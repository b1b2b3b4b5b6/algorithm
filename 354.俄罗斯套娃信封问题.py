#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

'''
不好做：
对w排序
对h排序
最终结果必然时上面两个序列的子序列
求最大子序列

对w递增排序（w相同时，h递减）
求h的最长递增子序列长度

'''


# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        def my_compare(l1, l2):
            if l1[0] > l2[0]:
                return 1

            if l1[0] < l2[0]:
                return -1

            if l1[0] == l2[0]:
                if l1[1] < l2[1]:
                    return 1
                if l1[1] > l2[1]:
                    return -1
                if l1[1] == l2[1]:
                    return 0
        import functools
        envelopes.sort(key=functools.cmp_to_key(my_compare))

        print(envelopes)

        target = [x[1] for x in envelopes]
        max_len = len(target)

        memo = [1] * len(target)

        for offset in range(len(target)):
            for n in range(0, offset):
                if target[n] < target[offset]:
                    memo[offset] = max(memo[offset], memo[n] + 1)

        return max(memo)
        # @lc code=end
