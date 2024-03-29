'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-14 11:00:09
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-14 11:28:00
FilePath: /leetcode/python/391.完美矩形.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=391 lang=python3
#
# [391] 完美矩形
#
# https://leetcode.cn/problems/perfect-rectangle/description/
#
# algorithms
# Hard (46.12%)
# Likes:    238
# Dislikes: 0
# Total Accepted:    25.1K
# Total Submissions: 54.5K
# Testcase Example:  '[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]'
#
# 给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi]
# 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。
#
# 如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。
#
#
# 示例 1：
#
#
# 输入：rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
# 输出：true
# 解释：5 个矩形一起可以精确地覆盖一个矩形区域。
#
#
# 示例 2：
#
#
# 输入：rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
# 输出：false
# 解释：两个矩形之间有间隔，无法覆盖成一个矩形。
#
# 示例 3：
#
#
# 输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
# 输出：false
# 解释：因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
#
#
#
# 提示：
#
#
# 1 <= rectangles.length <= 2 * 10^4
# rectangles[i].length == 4
# -10^5 <= xi, yi, ai, bi <= 10^5
#
#
#

# @lc code=start

'''
关键字
技巧

精确覆盖意味着：
矩形区域中不能有空缺，即矩形区域的面积等于所有矩形的面积之和；
矩形区域中不能有相交区域：判顶点出现次数
'''


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area, minX, minY, maxX, maxY = 0, rectangles[0][0], rectangles[0][1], rectangles[0][2], rectangles[0][3]
        cnt = defaultdict(int)
        for rect in rectangles:
            x, y, a, b = rect[0], rect[1], rect[2], rect[3]
            area += (a - x) * (b - y)

            minX = min(minX, x)
            minY = min(minY, y)
            maxX = max(maxX, a)
            maxY = max(maxY, b)

            cnt[(x, y)] += 1
            cnt[(x, b)] += 1
            cnt[(a, y)] += 1
            cnt[(a, b)] += 1

        if area != (maxX - minX) * (maxY - minY) or cnt[(minX, minY)] != 1 or cnt[(minX, maxY)] != 1 or cnt[(maxX, minY)] != 1 or cnt[(maxX, maxY)] != 1:
            return False

        del cnt[(minX, minY)], cnt[(minX, maxY)
                                   ], cnt[(maxX, minY)], cnt[(maxX, maxY)]

        return all(c == 2 or c == 4 for c in cnt.values())
