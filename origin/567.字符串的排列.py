#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (43.15%)
# Likes:    453
# Dislikes: 0
# Total Accepted:    117.8K
# Total Submissions: 272.9K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
#
# 换句话说，s1 的排列之一是 s2 的 子串 。
#
#
#
# 示例 1：
#
#
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#
#
# 示例 2：
#
#
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= s1.length, s2.length <= 10^4
# s1 和 s2 仅包含小写字母
#
#
#

# @lc code=start
'''
关键字
滑动窗口

字典(或者数组,因为只有26个英文字母)
注意边界
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for c in s1:
            if c not in d:
                d[c] = -1
            else:
                d[c] -= 1

        def check():
            for v in d.values():
                if v != 0:
                    return False
            return True
        for n in range(0, len(s2) - len(s1)+1):
            if n == 0:
                for i in range(len(s1)):
                    if s2[i] in d:
                        d[s2[i]] += 1

                    if check():
                        return True
            else:
                add_c = s2[n + len(s1) - 1]
                minus_c = s2[n-1]
                print(minus_c, add_c)

                if minus_c in d:
                    d[minus_c] -= 1

                if add_c in d:
                    d[add_c] += 1

                if check():
                    return True
        return False


# @lc code=end
