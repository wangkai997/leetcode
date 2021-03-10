#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        if root == None:
            return result

        layer = [root]
        while layer:
            temp = []
            size = len(layer)
            for i in range(size):
                item = layer.pop(0)
                temp.append(item.val)

                if item.left:
                    layer.append(item.left)
                if item.right:
                    layer.append(item.right)
            result.append(temp)

        return result


# @lc code=end
