'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-17 10:31:07
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-17 11:24:28
FilePath: /leetcode/python/432.全-o-1-的数据结构.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=432 lang=python3
#
# [432] 全 O(1) 的数据结构
#
# https://leetcode.cn/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (47.08%)
# Likes:    282
# Dislikes: 0
# Total Accepted:    27.3K
# Total Submissions: 58.1K
# Testcase Example:  '["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]\n' +
'[[],["hello"],["hello"],[],[],["leet"],[],[]]'
#
# 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。
#
# 实现 AllOne 类：
#
#
# AllOne() 初始化数据结构的对象。
# inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
# dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key
# 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
# getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
# getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。
#
#
# 注意：每个函数都应当满足 O(1) 平均时间复杂度。
#
#
#
# 示例：
#
#
# 输入
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey",
# "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# 输出
# [null, null, null, "hello", "hello", null, "hello", "leet"]
#
# 解释
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "leet"
#
#
#
#
# 提示：
#
#
# 1 <= key.length <= 10
# key 由小写英文字母组成
# 测试用例保证：在每次调用 dec 时，数据结构中总存在 key
# 最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 10^4 次
#
#
#

# @lc code=start

'''
关键字
双向链表
'''


class Node:

    def __init__(self, key, val) -> None:
        self.val = val
        self.key = key
        self.next = None
        self.last = None

    def Swap(left, right):
        last = left.last
        next = right.next

        last.next = right
        right.last = last
        right.next = left
        left.last = right
        left.next = next
        next.last = left

    def Insert(left, now):
        right = left.next
        left.next = now
        now.last = left
        now.next = right
        right.last = now

    def Delete(now):
        left = now.last
        right = now.next

        left.next = right
        right.last = left


class AllOne:

    def __init__(self):
        self.d = {}
        self.root = Node('root', -float('INF'))
        self.end = Node('end', float('INF'))
        self.root.next = self.end
        self.end.last = self.root

    def inc(self, key: str) -> None:
        if key not in self.d:
            now = Node(key, 1)
            self.d[key] = now
            Node.Insert(self.root, now)
        else:
            now = self.d[key]
            now.val += 1
            while now.val > now.next.val:
                Node.Swap(now, now.next)

    def dec(self, key: str) -> None:
        now = self.d[key]
        now.val -= 1
        if now.val == 0:
            self.d.pop(key)
            Node.Delete(now)
        else:
            while now.val < now.last.val:
                Node.Swap(now.last, now)

    def getMaxKey(self) -> str:
        if len(self.d) == 0:
            return ''

        return self.end.last.key

    def getMinKey(self) -> str:
        if len(self.d) == 0:
            return ''

        return self.root.next.key

       # Your AllOne object will be instantiated and called as such:
       # obj = AllOne()
       # obj.inc(key)
       # obj.dec(key)
       # param_3 = obj.getMaxKey()
       # param_4 = obj.getMinKey()
       # @lc code=end
