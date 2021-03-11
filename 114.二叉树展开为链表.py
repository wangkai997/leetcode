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
        def preorderTraversal(root: TreeNode):
            # if root:
            #     nodelist.append(root)
            #     preorderTraversal(root.left)
            #     preorderTraversal(root.right)
                return 
           

        nodelist=[]
        q = root
        preorderTraversal(root) 
        root = q
            
# @lc code=end

