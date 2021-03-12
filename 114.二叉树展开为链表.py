#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        prenode = None
        while stack:
            current = stack.pop()
            if prenode != None :
                prenode.left = None
                prenode.right = current
            left, right = current.left, current.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prenode = current
        

            
# @lc code=end

