#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = []
        def getvalue(root: TreeNode, num: int) -> int:
            # if not root:
            #     print(result)
            #     result.append(num)
            if root.left:
                getvalue(root.left, num*10+root.left.val)
            # else:
            #     result.append(num)
            if root.right:
                getvalue(root.right, num*10+root.right.val)
            if not root.left and not root.right:
                result.append(num)
        getvalue(root, root.val)
        # print(result)
        return sum(result)

        
        
        

# @lc code=end

