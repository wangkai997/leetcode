#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse(head,nexthead):
            pre,cur = None,head
            while cur!=nexthead:
                temp =cur.next
                cur.next= pre
                pre = cur
                cur = temp
            return pre,head
        if left==right:
            return head
        dis = right - left
        i = 0
        while i


# @lc code=end

