#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        def swap(nums,index1,index2):
            nums[index1],nums[index2] = nums[index2],nums[index1]

        n = len(nums)
        for i in range(n):
            while 1 <= nums[i]<=n and nums[i] != nums[nums[i]-1]:
                swap(nums,nums[i]-1,i)
        for i in range(n):
            if i != nums[i]-1:
                return i+1
        return n+1

        # n = len(nums)
        # for i in range(n):
        #     while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # for i in range(n):
        #     if nums[i] != i + 1:
        #         return i + 1
        # return n + 1



# @lc code=end

