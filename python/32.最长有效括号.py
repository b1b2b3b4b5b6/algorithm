'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-02 14:00:44
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-02 14:44:32
FilePath: /leetcode/python/32.最长有效括号.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode.cn/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (36.87%)
# Likes:    1984
# Dislikes: 0
# Total Accepted:    309.5K
# Total Submissions: 839.1K
# Testcase Example:  '"(()"'
#
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
#
#
#
#
# 示例 1：
#
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#
#
# 示例 2：
#
#
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#
#
# 示例 3：
#
#
# 输入：s = ""
# 输出：0
#
#
#
#
# 提示：
#
#
# 0
# s[i] 为 '(' 或 ')'
#
#
#
#
#

# @lc code=start
'''
关键字
双端遍历
'''




from audioop import reverse
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        left = 0
        right = 0
        out = 0
        for c in s:
            if c == '(':
                left += 1

            if c == ')':
                right += 1

            if right > left:
                left = 0
                right = 0

            if left == right:
                out = max(out, left + right)

        s: list = list(s)
        s.reverse()
        left = 0
        right = 0
        for c in s:
            if c == '(':
                left += 1

            if c == ')':
                right += 1

            if left > right:
                left = 0
                right = 0

            if left == right:
                out = max(out, left + right)
        return out
        # @lc code=end
