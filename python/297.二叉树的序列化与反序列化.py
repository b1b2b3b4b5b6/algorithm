'''
Author: b1b2b3b4b5b6 a1439458305@163.com
Date: 2022-10-02 22:31:22
LastEditors: b1b2b3b4b5b6 a1439458305@163.com
LastEditTime: 2022-10-03 15:51:56
FilePath: /leetcode/python/297.二叉树的序列化与反序列化.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (58.41%)
# Likes:    984
# Dislikes: 0
# Total Accepted:    186.1K
# Total Submissions: 318.7K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
#
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 /
# 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
#
# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode
# 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
#
#
# 示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
# 示例 4：
#
#
# 输入：root = [1,2]
# 输出：[1,2]
#
#
#
#
# 提示：
#
#
# 树中结点数在范围 [0, 10^4] 内
# -1000
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
关键字
递归
'''


class Codec:

    def serialize(self, root):
        if root == None:
            return ''
        out = []

        def dp(node):
            if node == None:
                return -1

            out.append(f'{node.val}|{dp(node.left)}|{dp(node.right)}')
            return len(out) - 1
        dp(root)
        res = ','.join(out)
        print(res)
        return res
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        sl = data.split(',')

        def dp(s: str):
            vl = s.split('|')
            my = TreeNode(int(vl[0]))
            left_index = int(vl[1])
            if left_index != -1:
                my.left = dp(sl[left_index])
            right_index = int(vl[2])
            if right_index != -1:
                my.right = dp(sl[right_index])
            return my
        return dp(sl[-1])
        # Your Codec object will be instantiated and called as such:
        # ser = Codec()
        # deser = Codec()
        # ans = deser.deserialize(ser.serialize(root))
        # @lc code=end
