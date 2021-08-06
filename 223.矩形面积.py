#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2-ax1)*(ay2-ay1)
        area2 = (bx2-bx1)*(by2-by1)

        # 计算重叠的面积
        x = max(0,min(ax2,bx2) - max(ax1,bx1))
        y = max(0,min(ay2,by2) - max(ay1,by1))
        return area1+area2-x*y

# @lc code=end

