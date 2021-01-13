'''
Author: your name
Date: 2020-12-30 01:56:58
LastEditTime: 2020-12-30 07:24:54
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode/146.lru-缓存机制.py
'''
#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start

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


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.order_dict = DoubleList()

    def get(self, key: int) -> int:
        if key not in self.order_dict:
            return - 1
        else:
            self.order_dict.move_to_end(key)
            return self.order_dict[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.order_dict and len(self.order_dict) >= self.capacity:
            self.order_dict.popitem(last=False)
        self.order_dict[key] = value
        self.order_dict.move_to_end(key)
        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        # @lc code=end


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.order_dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.order_dict:
            return - 1
        else:
            self.order_dict.move_to_end(key)
            return self.order_dict[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.order_dict and len(self.order_dict) >= self.capacity:
            self.order_dict.popitem(last=False)
        self.order_dict[key] = value
        self.order_dict.move_to_end(key)
