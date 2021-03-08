#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ## 先建一个数组 存中序遍历结果, 找最多两个不符合递增规律的值, 然后重新遍历原BFS树修改对应的值
        result=[]
        inorderTraversal(root, result)
        x, y = findError(result)
        
        def inorderTraversal(root, result):
            if root == None:
                return 
            inorderTraversal(root.left, result)
            result.append(root.val)
            inorderTraversal(root.right, result)

        def findError(result):
            flag = 0 
            for i in range(len(result)-1):
                if result[i] > result[i+1]: 
                    flag = flag + 1
                    if flag == 1:  
                        x, y = result[i], result[i+1]
                    if flag == 2:
                        y = result[i+1]
                        return x, y
            return x, y 
        def changeValue(root,x,y):






# @lc code=end

