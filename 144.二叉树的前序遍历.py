#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                result.append(node.val)
                node = node.left
            node = stack.pop()
            node = node.right
        return result
        
         

# @lc code=end

