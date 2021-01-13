'''
Author: your name
Date: 2021-01-06 06:19:35
LastEditTime: 2021-01-06 07:28:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/739.每日温度.py
'''
#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

'''
记录索引号
'''
# @lc code=start


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if T == []:
            return []
        stack = []
        res = {}
        for i in range(len(T)):
            if stack == []:
                stack.append(i)
            else:
                while len(stack) > 0 and T[i] > T[stack[-1]]:
                    res[stack[-1]] = i
                    stack.pop()
                stack.append(i)
        ret = [0] * len(T)
        for k, v in res.items():
            ret[k] = v - k
        return ret
        # @lc code=end
