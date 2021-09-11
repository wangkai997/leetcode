#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root=stack.pop()
            count+=1
            if count == k:
                return root.val
            root = root.right            


# @lc code=end

