#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
'''
关键字
二分查找

'''


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        piles.sort()
        l = len(piles)
        kmin = 1
        kmax = piles[-1]

        def get_res(temp):
            res = 0
            for v in piles:
                res += math.ceil(v/temp)
            return res

        while True:
            kmid = (kmin + kmax)//2
            res = get_res(kmid)

            if res > h:
                kmin = kmid
            if res <= h:
                kmax = kmid

            if kmax - kmin <= 1:
                if get_res(kmin) <= h:
                    return kmin
                else:
                    return kmax

# @lc code=end
