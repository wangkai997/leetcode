#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        cur,pre = head,None
        while cur!=None:
            temp = cur
            cur=cur.next
            temp.next = pre
            pre = temp
        return pre

# @lc code=end

