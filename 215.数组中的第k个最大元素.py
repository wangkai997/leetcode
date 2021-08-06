#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums,left,right):
            value_key = nums[right]
            while left<right:
                while nums[left]>=value_key and left<right:
                    left+=1
                nums[right] = nums[left]
                while nums[right]<value_key and left<right:
                    right-=1
                nums[left]= nums[right]
            nums[right] = value_key
            return right

        length = len(nums)
        left,right=0,length-1
        index = partition(nums,left,right)
        while index!=k-1:
            # 需要从大到小排序
            if index > k-1:
                index = partition(nums,left,index-1)
            else:
                index = partition(nums,index+1,right)
        return nums[index]
# @lc code=end

