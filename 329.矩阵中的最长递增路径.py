#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        result = 0
        m,n=len(matrix),len(matrix[0])
        flag=[[-1]*n for _ in range(m)]


        def dfs(matrix,i,j,flag):
            if flag[i][j]!=-1:
                return flag[i][j]
            else:
                d=1
                dirs=[[-1,0],[1,0],[0,-1],[0,1]]
                for dir in dirs:
                    x=i+dir[0]
                    y=j+dir[1]
                    if x>=0 and x<m and y>=0 and y<n and matrix[i][j]<matrix[x][y]:
                        d=max(d,dfs(matrix,x,y,flag)+1)
                flag[i][j]=d
                return d
        
        for i in range(m):
            for j in range(n):
                if flag[i][j] == -1:
                    result = max(result,dfs(matrix,i,j,flag))
        return result
# @lc code=end

