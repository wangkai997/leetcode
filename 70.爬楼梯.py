#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n 
        temp=[0]*n
        temp[0],temp[1]=1,2
        for i in range(2,n):
            temp[i]=temp[i-1]+temp[i-2]
        return temp[-1]


# @lc code=end

