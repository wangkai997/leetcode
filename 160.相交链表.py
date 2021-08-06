#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
<<<<<<< HEAD
        A,B = headA,headB
        while A!=B:
            A=A.next if A else headB
            B=B.next if B else headA
        return A
=======
>>>>>>> 95223625975d69fe90d8228e5d1a6b7dec3cdf7f
        
# @lc code=end

