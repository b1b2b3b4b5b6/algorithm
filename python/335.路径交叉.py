'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-09 15:10:41
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-09 15:35:49
FilePath: /leetcode/python/335.路径交叉.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=335 lang=python3
#
# [335] 路径交叉
#
# https://leetcode.cn/problems/self-crossing/description/
#
# algorithms
# Hard (42.57%)
# Likes:    157
# Dislikes: 0
# Total Accepted:    17.7K
# Total Submissions: 41.5K
# Testcase Example:  '[2,1,1,2]'
#
# 给你一个整数数组 distance 。
#
# 从 X-Y 平面上的点 (0,0) 开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动
# distance[2] 米，向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。
#
# 判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：distance = [2,1,1,2]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：distance = [1,2,3,4]
# 输出：false
#
#
# 示例 3：
#
#
# 输入：distance = [1,1,1,1]
# 输出：true
#
#
#
# 提示：
#
#
# 1 <= distance.length <= 10^5
# 1 <= distance[i] <= 10^5
#
#
#

# @lc code=start

'''
关键字
不会
'''


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        # n = len(distance)
        # for i in range(3, n):
        #     # 第 1 类路径交叉的情况
        #     if (distance[i] >= distance[i - 2]
        #             and distance[i - 1] <= distance[i - 3]):
        #         return True

        #     # 第 2 类路径交叉的情况
        #     if i == 4 and (distance[3] == distance[1]
        #                    and distance[4] >= distance[2] - distance[0]):
        #         return True

        #     # 第 3 类路径交叉的情况
        #     if i >= 5 and (distance[i - 3] - distance[i - 5] <= distance[i - 1] <= distance[i - 3]
        #                    and distance[i] >= distance[i - 2] - distance[i - 4]
        #                    and distance[i - 2] > distance[i - 4]):
        #         return True
        return False

# @lc code=end
