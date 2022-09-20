'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-19 17:56:54
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-20 12:47:18
FilePath: /leetcode/python/131.分割回文串.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode.cn/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (73.27%)
# Likes:    1268
# Dislikes: 0
# Total Accepted:    234.9K
# Total Submissions: 320.6K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#
# 回文串 是正着读和反着读都一样的字符串。
#
#
#
# 示例 1：
#
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#
#
# 示例 2：
#
#
# 输入：s = "a"
# 输出：[["a"]]
#
#
#
#
# 提示：
#
#
# 1
# s 仅由小写英文字母组成
#
#
#

# @lc code=start

'''
关键字
动态规划

状态：已截取的字符串列表 剩余的字符串
选择：截取剩余字符串的所有可能合法前缀

base_case：
    空字符串，加入结果

'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def check(temp_s):
            for i in range(0, len(temp_s) // 2):
                if temp_s[i] != temp_s[len(temp_s) - i-1]:
                    return False
            return True

        def dp(path: list, left):
            if len(left) == 0:
                res.append(path)
            for i in range(1, len(left)+1):
                prefix = left[:i]
                if check(prefix) == True:
                    new_path = list(path)
                    new_path.append(prefix)
                    dp(new_path, left[i:])
        dp([], s)
        return res
        # @lc code=end
