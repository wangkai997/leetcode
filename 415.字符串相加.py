#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # num1 存最短的
        if len(num2)< len(num1):
            num1,num2 = num2,num1
        result = ""
        index1,index2,add=len(num1)-1,len(num2)-1,0
        while index1>=0 or index2>=0:
            value1 = int(num1[index1]) if index1>=0 else 0
            value2 = int(num2[index2]) if index2>=0 else 0
            sum_value = value1 + value2 + add
            result = str(sum_value%10)+result
            add = sum_value//10
            index1,index2 = index1-1, index2-1
        if add>0:
            result = str(add) +result
        return result


        


# @lc code=end

