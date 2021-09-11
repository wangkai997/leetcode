#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set_value=set()
        n = len(nums)
        for i in range(n):
            if nums[i] in set_value:
                return True
            set_value.add(nums[i])
            if len(set_value)>k:
                set_value.remove(nums[i-k])
        return False
    # @lc code=end

