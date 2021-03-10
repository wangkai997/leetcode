#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 1 广度优先遍历
        # 2 深度优先遍历 
        # level = 0
        # def dfs(root, level, result):
        #     if not root:
        #         result.append(level)
        #         return 
        #     dfs(root.left, level+1, result)
        #     dfs(root.right, level+1, result)
        # result = []
        # dfs(root, level, result)
        # max_depth = max(result)
        # return max_depth

        # max_depth = 1 + max(left_depth, right_depth)
        def dfs(root):
            if not root:
                return 0
            return 1+ max(dfs(root.left),dfs(root.right))
        return dfs(root)

# @lc code=end
