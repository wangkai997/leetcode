#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        meet = None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                meet = slow
                break
        if meet == None:
            return None
        slow = head
        while slow!=meet:
            slow=slow.next
            meet=meet.next
        return meet
            
# @lc code=end

