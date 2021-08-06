#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        commen = strs[0]
        for string in strs[1:]:
            commen =self.lcp(commen,string)
            if commen == "":
                break
        return commen

    def lcp(self,string1,string2):
        length,index=min(len(string1),len(string2)),0
        
        while index<length and string1[index]==string2[index]:
            index += 1

        return string1[:index]
# @lc code=end

