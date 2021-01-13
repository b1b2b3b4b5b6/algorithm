'''
Author: your name
Date: 2021-01-06 08:34:08
LastEditTime: 2021-01-06 09:24:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/355.设计推特.py
'''
#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#

# @lc code=start


class Twitter:
    l = []
    links = {}

    def __init__(self):
        self.links = {}
        self.l = []
        """
        Initialize your data structure here.
        """

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.l.append([userId, tweetId])
        """
        Compose a new tweet.
        """

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        pool = [userId]
        if userId in self.links:
            pool = pool + self.links[userId]

        res = []
        for i in range(len(self.l) - 1, -1, -1):
            if len(res) >= 10:
                break
            if self.l[i][0] in pool:
                res.append(self.l[i][1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.links:
            self.links[followerId] = []

        fl = self.links[followerId]
        if followeeId in fl:
            return
        else:
            fl.append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.links:
            self.links[followerId] = []

        fl = self.links[followerId]
        if followeeId in fl:
            index = fl.index(followeeId)
            fl.pop(index)
        else:
            return

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
