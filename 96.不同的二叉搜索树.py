#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:

        if n <= 1:
            return 1
        return self.subTreeNumber(1,n+1)

    def subTreeNumber(self,start,end):
        if start >= end:
            return 1
        for i in range(start, end+1):
            left_number = self.subTreeNumber(start, i-1)
            right_number = self.subTreeNumber(i+1, end)
            
        
        pass 

# @lc code=end

