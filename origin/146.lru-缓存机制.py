#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (52.68%)
# Likes:    1616
# Dislikes: 0
# Total Accepted:    228.1K
# Total Submissions: 433.2K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
from typing import OrderedDict
'[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
#
#
#
# 实现 LRUCache 类：
#
#
# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value)
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
#
#
#
# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
#
#
# 示例：
#
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#
#
#
#
# 提示：
#
#
# 1
# 0
# 0
# 最多调用 2 * 10^5 次 get 和 put
#
#
#

# @lc code=start
'''
关键字
有序字典


字典
双向链表
可以直接使用python的有序字典OrderedDict
'''


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.d.keys():
            temp = self.d[key]
            self.d.pop(key)
            self.d[key] = temp
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d.keys():
            self.d.pop(key)

        if len(self.d) == self.capacity:
            self.d.popitem(last=False)

        self.d[key] = value

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        # @lc code=end
# 实现顺序字典


class Node:

    def __init__(self, prev, next, val, key):
        self.prev = prev
        self.next = next
        self.val = val
        self.key = key


class DoubleList:
    def __init__(self):
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.d = {}

    def add(self, node):
        node.next = self.tail
        node.prev = self.tail.prev

        node.prev.next = node
        node.next.prev = node

        self.size = self.size + 1

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size = self.size - 1

    def __contains__(self, key):
        if key in self.d:
            return True
        else:
            return False

    def __getitem__(self, key):
        return self.d[key].val

    def __setitem__(self, key, value):
        if key in self.d:
            self.d[key].val = value
        else:
            self.d[key] = Node(None, None, value, key)
            self.add(self.d[key])

    def __len__(self):
        return self.size

    def move_to_end(self, key):
        node = self.d[key]
        self.delete(node)
        self.add(node)

    def popitem(self, last=False):
        if last:
            node = self.tail.prev
        else:
            node = self.head.next
        del self.d[node.key]
        self.delete(node)
