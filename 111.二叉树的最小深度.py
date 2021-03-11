#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def getDepth(root: TreeNode) -> int:
            if not root:
                return 0

            # 没有左右孩子 则返回1
            if not root.left and not root.right:
                return 1
            # 左右孩子有一个为空 则返回1+最大的深度
            if root.left == None or root.right == None:
                return 1 + max(getDepth(root.left), getDepth(root.right))

            return 1 + min(getDepth(root.left), getDepth(root.right))
        return getDepth(root)
# @lc code=end
