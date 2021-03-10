#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        ## 两个指针 一个指向left 一个指向right
        def check(left,right):
            if left == None and right == None :
                return True
            if left == None or right == None :
                return False
            return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)
        if root == None:
            return True
        return check(root.left, root.right)
       
# @lc code=end

