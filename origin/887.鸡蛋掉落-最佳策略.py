#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#
# https://leetcode-cn.com/problems/super-egg-drop/description/
#
# algorithms
# Hard (29.16%)
# Likes:    687
# Dislikes: 0
# Total Accepted:    51.1K
# Total Submissions: 175.2K
# Testcase Example:  '1\n2'
#
# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
#
# 已知存在楼层 f ，满足 0  ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
#
# 每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1
# ）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
#
# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
#
#
# 示例 1：
#
#
# 输入：k = 1, n = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
# 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
# 如果它没碎，那么肯定能得出 f = 2 。
# 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。
#
#
# 示例 2：
#
#
# 输入：k = 2, n = 6
# 输出：3
#
#
# 示例 3：
#
#
# 输入：k = 3, n = 14
# 输出：4
#
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#

# @lc code=start

'''

关键字
动态规划 自定义


最坏情况的最少次数

最坏:碎了和没碎的最坏情况
最少:在最坏前提下的最优解


状态:dp(left_k, left_n)
    选择:
        遍历1-i扔鸡蛋,取最小
            碎了:dp(left_k-1, i-1) + 1
            没碎:dp(left_k, left_n - i) + 1
base_case:
    left_k = 1:
        return left_n
    left_n = 0:
        return 0
'''
memo = {}


def superEggDrop(k: int, n: int) -> int:

    def dp(left_k, left_n):
        if left_k == 1:
            return left_n
        if left_n == 0:
            return 0

        if (left_k, left_n) in memo:
            return memo[(left_k, left_n)][0]

        res = float('INF')

        start = 1
        end = left_n
        l = (left_k, left_n)
        while end >= start:
            mid = (end + start)//2
            broken_res = dp(left_k-1, mid-1) + 1
            not_broken_res = dp(left_k, left_n - mid) + 1

            if broken_res > not_broken_res:
                end = mid - 1
                if res <= broken_res:
                    None
                else:
                    l = (left_k-1, mid-1)
                    res = broken_res

            else:
                start = mid + 1
                if res <= not_broken_res:
                    None
                else:
                    l = (left_k, left_n - mid)
                    res = not_broken_res
        memo[(left_k, left_n)] = [res, l]

        return res

    return dp(k, n)


l = (2, 100)
print(superEggDrop(*l))

print(l)
while(l in memo):
    l = memo[l][1]
    print(100-l[1], l[0])

# @lc code=end
