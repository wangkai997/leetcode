#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        layer = [root]
        flag = 1
        while layer:
            temp = []
            size = len(layer)
            flag = flag + 1
            for i in range(size):
                item = layer.pop(0)
                temp.append(item.val)
                if item.left:
                    layer.append(item.left)
                if item.right:
                    layer.append(item.right)
            # 判断从左到右还是从右到左
            if flag % 2:
                temp = temp[::-1]
            result.append(temp)
        return result
                

# @lc code=end

