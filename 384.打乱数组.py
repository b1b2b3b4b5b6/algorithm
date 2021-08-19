#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.src = list(nums)

    def reset(self) -> List[int]:
        return self.src
        """
        Resets the array to its original configuration and return it.
        """

    def shuffle(self) -> List[int]:
        import random
        out = []
        temp = list(self.src)
        while len(temp) > 0:
            offset = random.randint(0, len(temp)-1)
            out.append(temp[offset])
            temp.pop(offset)
        return out
        """
        Returns a random shuffling of the array.
        """


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end
