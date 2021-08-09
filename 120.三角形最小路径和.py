#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        temp = [0]*n
        temp[0] = triangle[0][0]
        for i in range(1,n):
            temp[i] = temp[i-1]+triangle[i][i]
            for j in range(i-1,0,-1):
                temp[j] = min(temp[j-1],temp[j])+triangle[i][j]
            temp[0] += triangle[i][0]
        return min(temp)
                

# @lc code=end

