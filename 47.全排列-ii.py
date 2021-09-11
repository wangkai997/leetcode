#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def bfs(nums,start):
            if start == len(nums):
                result.append(nums[:])
            for i in range(start,len(nums)):
                

        
        result=[]
        bfs(nums,0)
        return result

# @lc code=end

