# @before-stub-for-debug-begin
from sys import tracebacklimit
from python3problem752 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
# https://leetcode-cn.com/problems/open-the-lock/description/
#
# algorithms
# Medium (53.02%)
# Likes:    397
# Dislikes: 0
# Total Accepted:    69.5K
# Total Submissions: 131K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8',
# '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
#
#
#
# 示例 1:
#
#
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
#
#
# 示例 2:
#
#
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：
# 把最后一位反向旋转一次即可 "0000" -> "0009"。
#
#
# 示例 3:
#
#
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# 输出：-1
# 解释：
# 无法旋转到目标数字且不被锁定。
#
#
# 示例 4:
#
#
# 输入: deadends = ["0000"], target = "8888"
# 输出：-1
#
#
#
#
# 提示：
#
#
# 1
# deadends[i].length == 4
# target.length == 4
# target 不在 deadends 之中
# target 和 deadends[i] 仅由若干位数字组成
#
#
#

# @lc code=start
'''
关键字
BFS
    BFS不需要比较最优值,因为先到先得
    注意起始值
'''


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        d = {}

        for s in deadends:
            num = int(s)
            d[num] = float('INF')

        change_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9]
        l = [0]
        if 0 in d:
            return -1
        d[0] = 0

        def dp(now):
            def get_all(n):
                res = []
                n1 = n//1000 % 10
                n2 = n//100 % 10
                n3 = n//10 % 10
                n4 = n % 10
                res.append(change_list[n1+1]*1000 + n % 1000)
                res.append(change_list[n1-1]*1000 + n % 1000)

                res.append(n1*1000 + change_list[n2+1]*100 + n % 100)
                res.append(n1*1000 + change_list[n2-1]*100 + n % 100)

                res.append(n1*1000 + n2*100 + change_list[n3+1]*10 + n % 10)
                res.append(n1*1000 + n2*100 + change_list[n3-1]*10 + n % 10)

                res.append(n1*1000 + n2*100 + n3*10 + change_list[n4+1])
                res.append(n1*1000 + n2*100 + n3*10 + change_list[n4-1])

                return res
            res = get_all(now)
            for num in res:
                if num in d:
                    continue

                d[num] = d[now] + 1
                l.append(num)

        while len(l) != 0:
            temp = list(l)
            l.clear()

            for n in temp:
                dp(n)

        target = int(target)

        if target not in d:
            return -1
        else:
            return d[target]


# @lc code=end
