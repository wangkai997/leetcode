#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getDepth(root: TreeNode) -> int:
            if not root:
                return 0
            leftdepth = getDepth(root.left)
            rightdepth = getDepth(root.right)
            if leftdepth == -1 or rightdepth == -1 or abs(leftdepth-rightdepth)>1:
                return -1
            else:
                return 1 + max(leftdepth, rightdepth)
        return getDepth(root) >= 0 
            
            


# @lc code=end

