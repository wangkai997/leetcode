#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # ## 方法一 递归
        # def check(root, min=-float("inf"), max=float("inf")):
        #     if not root:
        #         return True

        #     if root.val <= min or root.val>= max:
        #         return False

        #     if check(root.left, min, root.val) == False:
        #         return False
        #     if check(root.right, root.val, max) == False:
        #         return False
        #     return True

        # return check(root)


        # 方法二 使用中序遍历
        def inorderTraversal(root, result):
            if root == None:
                return
            inorderTraversal(root.left, result)
            result.append(root.val)
            inorderTraversal(root.right, result)

        if root == None:  # 空树
            return True
        result = []
        inorderTraversal(root, result)
        for i in range(len(result)-1):
            if result[i] >= result[i+1]:
                return False
        return True


# @lc code=end
