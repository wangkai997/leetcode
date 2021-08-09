#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1],matrix[n-j-1][i]=matrix[n-j-1][i],matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1]
        return matrix


# @lc code=end

