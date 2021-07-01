#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#


'''
从后往前翻
'''
# @lc code=start


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        now = list(arr)
        target = list(now)
        target.sort()
        out = []

        for n in range(len(target) - 1, -1, -1):
            val = target[n]
            index = now.index(val)
            if index == val:
                continue

            temp = now[:index + 1]
            temp.reverse()
            now = temp + now[index + 1:]
            out.append(index + 1)

            temp = now[:n + 1]
            temp.reverse()
            now = temp + now[n + 1:]
            out.append(n + 1)

        if now != target:
            print(now, target)
        return out
        # @lc code=end
