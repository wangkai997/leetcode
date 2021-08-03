#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        if m == 0:
            return 0
        if m == 1:
            return nums[0]
        temp = [0] * m
        temp[0]=nums[0]
        temp[1] = max(nums[1],nums[0])

        for i in range(2,m):
            temp[i] = max(temp[i-1],temp[i-2]+nums[i])
        return temp[-1]


# @lc code=end

