#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 动态规划
        n = len(height)
        left_height = [0]*n
        right_height = [0]*n
        left_height[0]=height[0]
        right_height[-1]=height[-1]
        for i in range(1,n):
            left_height[i] = max(left_height[i-1],height[i])
        for j in range(n-2,-1,-1):
            right_height[j]=max(right_height[j+1],height[j])
        result = 0
        for i in range(n):
            result+=min(left_height[i],right_height[i])-height[i]
        return result

        # 双指针来优化空间复杂度
        


# @lc code=end

