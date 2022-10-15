'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-07 18:18:48
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-08 18:38:10
FilePath: /leetcode/python/330.按要求补齐数组.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=330 lang=python3
#
# [330] 按要求补齐数组
#
# https://leetcode.cn/problems/patching-array/description/
#
# algorithms
# Hard (52.97%)
# Likes:    332
# Dislikes: 0
# Total Accepted:    21.5K
# Total Submissions: 40.6K
# Testcase Example:  '[1,3]\n6'
#
# 给定一个已排序的正整数数组 nums ，和一个正整数 n 。从 [1, n] 区间内选取任意个数字补充到 nums 中，使得 [1, n]
# 区间内的任何数字都可以用 nums 中某几个数字的和来表示。
#
# 请返回 满足上述要求的最少需要补充的数字个数 。
#
#
#
# 示例 1:
#
#
# 输入: nums = [1,3], n = 6
# 输出: 1
# 解释:
# 根据 nums 里现有的组合 [1], [3], [1,3]，可以得出 1, 3, 4。
# 现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
# 其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖 [1, 6] 区间里所有的数。
# 所以我们最少需要添加一个数字。
#
# 示例 2:
#
#
# 输入: nums = [1,5,10], n = 20
# 输出: 2
# 解释: 我们需要添加 [2,4]。
#
#
# 示例 3:
#
#
# 输入: nums = [1,2,2], n = 5
# 输出: 0
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# nums 按 升序排列
# 1 <= n <= 2^31 - 1
#
#
#

# @lc code=start

'''
关键字
技巧
此题难在厘清思路，实际上我们要做的是维护一个当前能用和表示的最大数字ach，然后根据数组的值来判断需不需要插值。要理解这题的解法，需要先弄明白一个非常关键的道理：

一个数组[a1,a2,a3...an]当前能用和表示的数字区间为[1,ach]，此时往数组内补充新数num，则此时能表示的区间为[1,ach]∪[num,ach + num]

要理解这一点并不复杂，首先由于num被添加进了数组，则能实现的最大的数显然变成了ach + num，而由于ach之前的数[1, ach]都可以通过和实现，那么要实现ach + num - k（k <= ach），只需要从ach + num的组合里把和为k的组合拿掉即可。那么同理，实现[num,ach + num]就相当于用ach + num依次减掉[1,ach]中的数字，显然可以办到。

本题的贪心思想即来源于此，为了使补充的新数物尽其用，能够直接扩大可表示的区间范围，把补充的num设为ach + 1即可。此时能表示的数字区间可以直接更新为[1, ach + ach + 1]，不会漏掉中间的数字。

所以本题的思路是这样的：

当前能表示的最大数字为ach，则下一个需要达到的目标数字是ach + 1，而当前（未使用）的数组元素为num = nums[idx]
判断num与目标值ach + 1的大小关系，如果num > ach + 1，则：
说明[ach + 1, num - 1]区间内的数字无法表示，必须补充插入新数
为了使插入的新数既能表示ach + 1，又能尽可能覆盖更多的数组（贪心的关键之处），插入的数字就是ach + 1
插入ach + 1之后，更新ach = ach + ach + 1
如果num < ach + 1，说明当前的目标值ach + 1必然可以实现（因为num >= 1），此时更新ach = ach + num

'''


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = []

        arch = 0

        i = 0
        while True:
            if arch >= n:
                print(res)
                return len(res)

            if i == len(nums):
                arch += arch + 1
                res.append(arch+1)
                continue

            num = nums[i]

            if num <= arch + 1:
                arch += num
                i += 1
            else:
                arch += arch + 1
                res.append(arch+1)

        # @lc code=end
