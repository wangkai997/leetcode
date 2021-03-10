#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def ArrayToBST(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            if len(nums) > 1:
                mid = len(nums)//2
                root = TreeNode(nums[mid])
                root.left = ArrayToBST(nums[:mid])
                root.right = ArrayToBST(nums[mid+1:])
                return root
        # root = TreeNode()
        root = ArrayToBST(nums[:])
        return root
# @lc code=end

