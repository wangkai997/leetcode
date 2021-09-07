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
        
        self.cur = 0
        self.topk = 0

        def inorder(root,k):
            if root == None:
                return 
            inorder(root.left,k)
            self.cur += 1
            if self.cur == k:
                self.topk = root.val
                return
            inorder(root.right,k)


        inorder(root,k)
        return self.topk 

# @lc code=end

