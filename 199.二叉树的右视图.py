#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        layer = []
        result = []
        if root == None:
            return result
        layer.append(root)
        
        while layer:
            temp = []
            size = len(layer)
            value = None
            for i in range(size):
                node = layer.pop(0)
                value = node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            layer=temp
            result.append(value)
        return result
        
                




# @lc code=end

