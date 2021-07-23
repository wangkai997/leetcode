#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        ispositive = True
        integer_part = []
        decimal_part = []
        s = s.strip() # 去掉左边的空格
        for i in s:
            
# @lc code=end

