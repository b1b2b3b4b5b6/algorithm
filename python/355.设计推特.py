#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#
# https://leetcode-cn.com/problems/design-twitter/description/
#
# algorithms
# Medium (40.70%)
# Likes:    255
# Dislikes: 0
# Total Accepted:    26.4K
# Total Submissions: 64.9K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n' +
'[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
#
# 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：
#
#
# postTweet(userId, tweetId): 创建一条新的推文
# getNewsFeed(userId):
# 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
# follow(followerId, followeeId): 关注一个用户
# unfollow(followerId, followeeId): 取消关注一个用户
#
#
# 示例:
#
#
# Twitter twitter = new Twitter();
#
# // 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
# twitter.postTweet(1, 5);
#
# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# twitter.getNewsFeed(1);
#
# // 用户1关注了用户2.
# twitter.follow(1, 2);
#
# // 用户2发送了一个新推文 (推文id = 6).
# twitter.postTweet(2, 6);
#
# // 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
# // 推文id6应当在推文id5之前，因为它是在5之后发送的.
# twitter.getNewsFeed(1);
#
# // 用户1取消关注了用户2.
# twitter.unfollow(1, 2);
#
# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# // 因为用户1已经不再关注用户2.
# twitter.getNewsFeed(1);
#
#
#

# @lc code=start

'''
关键字
硬写
'''


class Twitter:

    def __init__(self):
        self.tlist = []
        self.fdict = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tlist.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[str]:
        if userId not in self.fdict.keys():
            self.fdict[userId] = [userId]

        out_list = []
        for n in range(len(self.tlist) - 1, -1, -1):
            v = self.tlist[n]
            if v[0] in self.fdict[userId]:
                out_list.append(v[1])
                if len(out_list) == 10:
                    break
        return out_list

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.fdict.keys():
            self.fdict[followerId] = [followerId]

        self.fdict[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.fdict.keys():
            self.fdict[followerId] = [followerId]

        if followeeId not in self.fdict[followerId]:
            return

        i = self.fdict[followerId].index(followeeId)
        self.fdict[followerId].pop(i)
       # Your Twitter object will be instantiated and called as such:
       # obj = Twitter()
       # obj.postTweet(userId,tweetId)
       # param_2 = obj.getNewsFeed(userId)
       # obj.follow(followerId,followeeId)
       # obj.unfollow(followerId,followeeId)
       # @lc code=end
