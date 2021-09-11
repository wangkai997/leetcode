#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
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
        temp = root
        while True:
            if temp.val>p.val and temp.val>q.val:
                temp = temp.left
            elif temp.val< p.val and temp.val<q.val:
                temp = temp.right
            else:
                return temp

        


# @lc code=end

