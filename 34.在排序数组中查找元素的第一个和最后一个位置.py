#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findstart(nums,target):
            l,r = 0,len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]< target:
                    l = mid+1
                else:
                    r = mid -1
            return l

        def findend(nums,target):
            index = len(nums)-1
            l,r = 0,len(nums)-1
            while l<=r:
                mid = (l+r) // 2
                if nums[mid] <= target:
                    l = mid+1
                else:
                    r = mid -1
            return l-1

        start = findstart(nums,target)
        if len(nums)==start or nums[start]!=target:
            return [-1,-1]
        end = findend(nums,target)
        return [start,end]

# @lc code=end

