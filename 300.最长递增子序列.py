#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # # method 1 动态规划
        # n = len(nums)
        # if n <= 1:
        #     return n
        # # 使用动态规划
        # # dp[i] 表示：以 nums[i] 结尾 的「上升子序列」的长度。注意：这个定义中 nums[i] 必须被选取，且必须是这个子序列的最后一个元素
        # # 时间O(n^2) 空间O(n)
        # dp = []
        # for i in range(n):
        #     dp.append(1)
        #     for j in range(i):
        #         if nums[i]>nums[j]:
        #             dp[i] = max(dp[j]+1,dp[i])
        # return max(dp)

        # method 2 贪心+二分法
         
        # d[i],表示长度为 i 的最长上升子序列的末尾元素的最小值，用 len 记录目前最长上升子序列的长度，
        tail = []
        length = len(nums)
        for value in nums:
            if not tail or value>tail[-1]:
                tail.append(value)
            else:
                l,r=0,len(tail)-1
                cur = r
                while l<=r:
                    mid = (l+r)//2
                    if tail[mid] >=value:
                        r = mid - 1
                        cur = mid
                    else:
                        l = mid + 1
                tail[cur] = value
        return len(tail)



# @lc code=end

