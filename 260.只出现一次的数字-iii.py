#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n<=2:
            return nums
        result = []
        temp = nums[0]
        for i in range(1,n):
            temp = temp^nums[i]
        
        # 找从最低位第一个不为0的
        div = 1
        while div&temp==0:
            div = div<<1
        a,b =0,0
        for value in nums:
            if div&value!=0:
                a = a^value
            else:
                b = b^value
        return [a,b]
        
# @lc code=end

