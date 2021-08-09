#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        temp = [[0]*n for i in range(m)] 
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    temp[i][j]=0
                else:
                    if i == 0 and j==0:
                        temp[i][j]=1
                    else:
                        # 处理上边入口
                        a = temp[i-1][j] if i!=0 else 0
                        # 处理左边入口
                        b = temp[i][j-1] if j!=0 else 0
                        temp[i][j] = a+b
        return temp[-1][-1]
                
# @lc code=end

