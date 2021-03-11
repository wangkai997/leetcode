#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        def helper(root: TreeNode, targetSum: int, path):
            if not root:
                return 
            path.append(root.val)
            if root.left == None and root.right == None and targetSum == root.val:
                result.append(path[:])
            helper(root.right, targetSum-root.val, path) 
            helper(root.left, targetSum-root.val, path)
            path.pop()



        result = []
        path = []
        helper(root, targetSum, path)
        return result

# @lc code=end

