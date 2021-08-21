#
# @lc app=leetcode.cn id=261 lang=python3
#
# [261] 以图判树
#

# @lc code=start
'''
注意点：合法树
    结点数要全
    只有一个结点的总是合法
    树结构不存在闭合圈
'''


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = {}
        if n == 1:
            return True

        def find_root(x):
            if m[x] == x:
                return x
            else:
                return find_root(m[x])

        for l in edges:
            a = l[0]
            b = l[1]
            if a in m and b in m:
                if find_root(a) == find_root(b):
                    return False
            if a not in m:
                m[a] = a
            if b not in m:
                m[b] = b

            m[find_root(a)] = find_root(b)

        count = 0
        for k, v in m.items():
            if k == v:
                count += 1
        if count == 1:
            for i in range(n):
                if i not in m:
                    return False
            return True
        else:
            return False

            # @lc code=end
