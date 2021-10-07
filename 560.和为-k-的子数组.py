#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
'''
前缀和

发现普通遍历超时,用字典
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
