#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1:
            return len(s)
        substring=[]
        for i in range(len(s)-1):
            max_len = 0
            for j in range((i),len(s)):
                if s[j] not in s[i:j]:
                    max_len += 1
                else:
                    substring.append(max_len)
                    break
        return max(substring)
            

 # @lc code=end

