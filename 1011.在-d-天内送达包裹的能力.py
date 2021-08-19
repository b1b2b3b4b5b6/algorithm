#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

'''
最高效情况下的解
    应从最大的开始运，然后按顺序尽量填充其他
'''

# @lc code=start


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        origin = list(weights)
        weights.sort(reverse=True)
        sum = 0
        for w in weights:
            sum += w
        dmin = weights[0]
        dmax = sum

        def check(v):
            ret = 1
            left_v = v
            for w in origin:
                left_v -= w
                if left_v >= 0:
                    continue
                if left_v < 0:
                    ret += 1
                    left_v = v - w
            return ret

        dmid = (dmin + dmax) // 2

        while dmin < dmax:

            ret = check(dmid)
            if ret <= days:
                dmax = dmid
            if ret > days:
                dmin = dmid + 1
            dmid = (dmin + dmax) // 2

        return dmin

        # @lc code=end
