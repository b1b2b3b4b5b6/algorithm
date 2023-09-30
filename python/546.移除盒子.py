#
# @lc app=leetcode.cn id=546 lang=python3
#
# [546] 移除盒子
#
# https://leetcode.cn/problems/remove-boxes/description/
#
# algorithms
# Hard (60.70%)
# Likes:    400
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 30.8K
# Testcase Example:  '[1,3,2,2,2,3,4,3,1]'
#
# 给出一些不同颜色的盒子 boxes ，盒子的颜色由不同的正数表示。
# 
# 你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k * k
# 个积分。
# 
# 返回 你能获得的最大积分和 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：boxes = [1,3,2,2,2,3,4,3,1]
# 输出：23
# 解释：
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
# ----> [1, 3, 3, 3, 1] (1*1=1 分) 
# ----> [1, 1] (3*3=9 分) 
# ----> [] (2*2=4 分)
# 
# 
# 示例 2：
# 
# 
# 输入：boxes = [1,1,1]
# 输出：9
# 
# 
# 示例 3：
# 
# 
# 输入：boxes = [1]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= boxes.length <= 100
# 1 <= boxes[i] <= 100
# 
# 
#

# @lc code=start
'''
关键字
动态规划

'''

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        i = 0
        dl = []
        while i < len(boxes):
            num = boxes[i]

            end = len(boxes)
            for j in range(i, len(boxes)):
                if boxes[j] == boxes[i]:
                    continue
                else:
                    end = j
                    break
            dl.append([num, end - i])
            i = end
        print(dl)

        mem = {}

        def dp(left, right, k):
            if left >= right:
                return 0
            if (left, right, k) in mem:
                return mem[(left, right, k)]
            num = dl[left][0]
            count = dl[left][1] + k
            ret = dp(left+1, right, 0) + count ** 2
            for i in range(left + 1, right):
                cup = dl[i]
                if cup[0] != num:
                    continue

                ret = max(ret, dp(left+1, i, 0) + dp(i, right, count))
            mem[(left, right, k)] = ret
            return ret
        res = dp(0, len(dl), 0)
        return res
# @lc code=end

