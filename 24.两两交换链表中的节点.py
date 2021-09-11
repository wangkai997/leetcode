#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(head,tail):
            tail.next = head
            return tail
        if not head or not head.next:
            return head
        newhead = head.next
        nexthead = newhead.next
        newhead.next = head
        head.next = self.swapPairs(nexthead)
        return newhead

# @lc code=end

