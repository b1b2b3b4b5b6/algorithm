#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#

# @lc code=start
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        m = {}

        def find_root(x):
            if m[x] == x:
                return x
            else:
                return find_root(m[x])

        for s in equations:
            a = s[0]
            b = s[3]

            if s[1] == '=':

                if a not in m:
                    m[a] = a
                if b not in m:
                    m[b] = b
                if a == b:
                    continue

                m[find_root(b)] = find_root(a)

        for s in equations:
            a = s[0]
            b = s[3]

            if s[1] == '!':
                if a == b:
                    return False
                if a not in m or b not in m:
                    continue
                if find_root(a) == find_root(b):
                    return False
        return True

        # @lc code=end
