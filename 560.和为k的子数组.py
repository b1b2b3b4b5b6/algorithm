#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start

'''
现以每一个数字为开始，向后遍历寻找合法数组：
    找到：在合法数组后统计sum为0的次数
    没找到：下一个

此方法超时，算法复杂度n2，考虑优化

'''

'''
前缀和：提前算好sum[i]的值，则sum(i,j] = sum[j] - sum[i]

原始方法超时，考虑优化

前缀和数组转为map，sum为key，偏移为value

'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        l = len(nums)
        pre = [0 for n in range(l+1)]
        for n in range(l):
            pre[n + 1] = pre[n] + nums[n]

        map_pre = {}
        for n in range(len(pre)):
            key = pre[n]
            if key not in map_pre.keys():
                map_pre[key] = [n]
            else:
                map_pre[key].append(n)

        for start in range(l + 1):
            end_value = k + pre[start]
            if end_value in map_pre.keys():
                for n in map_pre[end_value]:
                    if n > start:
                        res += 1
        return res
        # @lc code=end
