#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def findMax(nums):
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            dp = [0] *n
            dp[0]=nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,n):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])

            pass
            return dp[-1]
        
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        # 环形就分开考虑
        return max(findMax(nums[:-1]),findMax(nums[1:]))

# @lc code=end

