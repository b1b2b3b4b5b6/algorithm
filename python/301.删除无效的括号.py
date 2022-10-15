#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#
# https://leetcode.cn/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (55.16%)
# Likes:    774
# Dislikes: 0
# Total Accepted:    83.5K
# Total Submissions: 151.4K
# Testcase Example:  '"()())()"'
#
# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
#
# 返回所有可能的结果。答案可以按 任意顺序 返回。
#
#
#
# 示例 1：
#
#
# 输入：s = "()())()"
# 输出：["(())()","()()()"]
#
#
# 示例 2：
#
#
# 输入：s = "(a)())()"
# 输出：["(a())()","(a)()()"]
#
#
# 示例 3：
#
#
# 输入：s = ")("
# 输出：[""]
#
#
#
#
# 提示：
#
#
# 1
# s 由小写英文字母以及括号 '(' 和 ')' 组成
# s 中至多含 20 个括号
#
#
#

# @lc code=start


'''
关键字
BFS

'''


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(temp):
            num = 0
            for i in temp:
                if i == '(':
                    num += 1
                if i == ')':
                    num -= 1
                    if num < 0:
                        return False
            if num != 0:
                return False
            return True

        ans = []
        currSet = set([s])

        while True:
            for ss in currSet:
                if isValid(ss):
                    ans.append(ss)
            if len(ans) > 0:
                return ans
            nextSet = set()
            for ss in currSet:
                for i in range(len(ss)):
                    if i > 0 and ss[i] == s[i - 1]:
                        continue
                    if ss[i] == '(' or ss[i] == ')':
                        nextSet.add(ss[:i] + ss[i + 1:])
            currSet = nextSet
        return ans


# @lc code=end
