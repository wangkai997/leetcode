#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def generatesubtree(start,end):
            result = []
            if start > end:
                result.append(None)
                return result
            for i in range(start,end+1):
                left_trees = generatesubtree(start,i-1)
                right_trees = generatesubtree(i+1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        result.append(root)
                        
            return result

        if n <= 0:
            return []

        return generatesubtree(1,n)


# @lc code=end

