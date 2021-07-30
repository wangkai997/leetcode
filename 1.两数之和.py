#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        for index,value in enumerate(nums):
            if hashmap.get(target-value) is not None:
                return [index,hashmap.get(target-value)]

            hashmap[value]=index

# @lc code=end

