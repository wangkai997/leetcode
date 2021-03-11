#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def helper(root: TreeNode, targetSum: int) -> int:
            if not root:
                return False

            # 到叶子节点的路径和 是不是目标
            if root.left == None and root.right == None: 
                return targetSum == root.val
            if root.left == None:
                return helper(root.right, targetSum-root.val)
            if root.right == None:
                return helper(root.left, targetSum-root.val)

            return helper(root.left, targetSum-root.val) or helper(root.right, targetSum-root.val)
        
        return helper(root, targetSum)
# @lc code=end

