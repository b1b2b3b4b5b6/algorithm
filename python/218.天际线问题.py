'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-09-26 23:52:11
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-09-27 12:09:48
FilePath: /leetcode/python/218.天际线问题.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#
# https://leetcode.cn/problems/the-skyline-problem/description/
#
# algorithms
# Hard (55.16%)
# Likes:    721
# Dislikes: 0
# Total Accepted:    43.9K
# Total Submissions: 79.5K
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
# 城市的 天际线 是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回 由这些建筑物形成的 天际线 。
#
# 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti]
# 表示：
#
#
# lefti 是第 i 座建筑物左边缘的 x 坐标。
# righti 是第 i 座建筑物右边缘的 x 坐标。
# heighti 是第 i 座建筑物的高度。
#
#
# 你可以假设所有的建筑都是完美的长方形，在高度为 0 的绝对平坦的表面上。
#
# 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序
# 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0
# ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
#
# 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...]
# 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
#
#
#
# 示例 1：
#
#
# 输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# 输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# 解释：
# 图 A 显示输入的所有建筑物的位置和高度，
# 图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。
#
# 示例 2：
#
#
# 输入：buildings = [[0,2,3],[2,5,3]]
# 输出：[[0,3],[5,0]]
#
#
#
#
# 提示：
#
#
# 1 <= buildings.length <= 10^4
# 0 <= lefti < righti <= 2^31 - 1
# 1 <= heighti <= 2^31 - 1
# buildings 按 lefti 非递减排序
#
#
#

# @lc code=start
'''
关键字
遍历 优先级队列
'''




from distutils.command.build import build
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        xl = {}
        for i in range(len(buildings)):
            b = buildings[i]
            if b[0] not in xl:
                xl[b[0]] = []
            xl[b[0]].append(i)

            if b[1] not in xl:
                xl[b[1]] = []
            xl[b[1]].append(i)

        kl = list(xl.keys())
        kl.sort()
        print(kl)
        res = []
        hl = []
        for x in kl:

            for offset in xl[x]:
                if buildings[offset][1] == x:
                    hl.remove(offset)

            for offset in xl[x]:
                if buildings[offset][0] == x:
                    b = buildings[offset]

                    hl.append(offset)
                    hl.sort(key=lambda x: buildings[x][2])

            if len(hl) == 0:
                temp_res = 0
            else:
                temp_res = buildings[hl[-1]][2]
            if len(res) == 0:
                res.append((x, temp_res))

            if res[-1][1] != temp_res:
                res.append((x, temp_res))

        return res
        # @lc code=end
