#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # method 1
        # dic = DefaultDict(int)
        # for value in nums:
        #     dic[value] += 1
        # return max(dic,key=dic.get)

        # # method 2
        # nums = sorted(nums)
        # return nums[len(nums)//2]

        # metthod 3
        candidate = None
        count = 0

        for item in nums:
            if count == 0:
                candidate = item
                count = 1
            else:
                if candidate!= item:
                    count -= 1
                else:
                    count += 1
        return candidate




# @lc code=end

