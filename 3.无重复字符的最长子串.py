#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) <=1:
        #     return len(s)
        # substring=[]
        # for i in range(len(s)-1):
        #     max_len = 0
        #     for j in range((i),len(s)):
        #         if s[j] not in s[i:j]:
        #             max_len += 1
        #         else:
        #             substring.append(max_len)
        #             break
        # return max(substring)

        # 方法二
        length = len(s)
        if length<=1:
            return length
        current_string = set()
        left=0
        max_len = 0
        cur_len = 0
        for i in range(length):
            cur_len += 1
            while s[i] in current_string:
                cur_len -=1
                current_string.remove(s[left])
                left += 1
            current_string.add(s[i])
            max_len = max(max_len,cur_len)
        return max_len
            

            

 # @lc code=end

