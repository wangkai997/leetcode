#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        length = len(nums)
        for first in range(length):
            if first>0 and nums[first]==nums[first-1]:
                continue
            else:
                target = - nums[first]
                third = length-1
                for second in range(first+1,length-1):
                    if second>first+1 and nums[second]==nums[second-1]:
                        continue
                    while second<third and nums[second]+nums[third]>target:
                        third-=1
                    if second == third:
                        break
                    if nums[second]+nums[third]==target:
                        result.append([nums[first],nums[second],nums[third]])
        return result



# @lc code=end

