#
# @lc app=leetcode.cn id=855 lang=python3
#
# [855] 考场就座
#

# @lc code=start
class ExamRoom:

    def __init__(self, n: int):
        self.m = []
        self.l = n

    def seat(self) -> int:
        if len(self.m) == 0:
            res = [0, 0]
        else:
            self.m.sort()
            res = [-1, -1]
            dump = list(self.m)
            dump.append(-self.m[0])
            dump.append(self.l - 1 + (self.l - 1 - self.m[-1]))
            dump.sort()
            for k, v in enumerate(dump):

                if k == 0:
                    continue

                start = dump[k-1]
                end = dump[k]
                bet = (end - start) // 2
                offset = start + bet

                if bet > res[1]:
                    res[1] = bet
                    res[0] = offset

        self.m.append(res[0])
        return res[0]

    def leave(self, p: int) -> None:
        i = self.m.index(p)
        self.m.pop(i)

        # Your ExamRoom object will be instantiated and called as such:
        # obj = ExamRoom(n)
        # param_1 = obj.seat()
        # obj.leave(p)
        # @lc code=end
