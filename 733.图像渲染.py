#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        old = image[sr][sc]
        res = []

        def flip(x, y):
            if x >= len(image[0]) or x < 0:
                return

            if y >= len(image) or y < 0:
                return

            if image[y][x] != old:
                return

            if image[y][x] == newColor:
                return

            image[y][x] = newColor

            tub = [(x, y+1), (x+1, y), (x-1, y), (x, y-1)]
            for t in tub:
                flip(t[0], t[1])
        flip(sc, sr)
        return image
        # @lc code=end
