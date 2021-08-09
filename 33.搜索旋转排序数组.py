#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        if n<1:
            return -1
        l,r=0,n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid]>=nums[0]:
                    if nums[l]<= target< nums[mid]:
                        r = mid-1
                    else:
                        l = mid +1
                else:
                    if nums[mid] < target <= nums[n-1]:
                        l = mid+1
                    else:
                        r = mid - 1
        return -1
                    

# @lc code=end

