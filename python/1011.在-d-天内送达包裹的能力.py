#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#
# https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/description/
#
# algorithms
# Medium (62.67%)
# Likes:    396
# Dislikes: 0
# Total Accepted:    60.1K
# Total Submissions: 96K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10]\n5'
#
# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
#
# 传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。
#
# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。
#
#
#
# 示例 1：
#
#
# 输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# 输出：15
# 解释：
# 船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
# 第 1 天：1, 2, 3, 4, 5
# 第 2 天：6, 7
# 第 3 天：8
# 第 4 天：9
# 第 5 天：10
#
# 请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9),
# (10) 是不允许的。
#
#
# 示例 2：
#
#
# 输入：weights = [3,2,2,4,1,4], D = 3
# 输出：6
# 解释：
# 船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
# 第 1 天：3, 2
# 第 2 天：2, 4
# 第 3 天：1, 4
#
#
# 示例 3：
#
#
# 输入：weights = [1,2,3,1,1], D = 4
# 输出：3
# 解释：
# 第 1 天：1
# 第 2 天：2
# 第 3 天：3
# 第 4 天：1, 1
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
二分查找

二分法(闭合区间,在左右搜寻)
二分法(左边界)
'''


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = max(weights)
        left = max_weight
        right = sum(weights)

        def check(mid):
            res = 0
            tmp = 0
            for w in weights:
                if tmp + w > mid:
                    res += 1
                    tmp = w
                else:
                    tmp += w
            res += 1
            return res

        while left < right:
            # import math
            # mid = math.ceil((left+right) / 2)
            mid = (left+right) // 2  # 左边界需要向下取整
            res = check(mid)
            if res == days:
                right = mid
            elif res > days:
                left = mid + 1
            elif res < days:
                right = mid

        return left
        # @lc code=end
