#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root == None or root == p or root == q:
            return root
        is_left = self.lowestCommonAncestor(root.left, p, q)
        is_right = self.lowestCommonAncestor(root.right, p, q)
        if is_left!=None and is_right != None:
            return root
        if is_left != None and is_right == None:
            return is_left
        if is_left == None and is_right != None:
            return is_right
        return None




# @lc code=end

