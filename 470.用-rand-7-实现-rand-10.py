#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7()-1)*7+rand7() 
        while num>40:
            num = (rand7()-1)*7+rand7()
        return 1+(num-1)%10
        
        
# @lc code=end

