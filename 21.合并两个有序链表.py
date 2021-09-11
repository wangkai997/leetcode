#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val<=l2.val:
                newhead = l1
                l1 = l1.next

                newhead.next = self.mergeTwoLists(l1,l2)
                return newhead
            else:
                newhead = l2
                l2 = l2.next
                newhead.next = self.mergeTwoLists(l1,l2)
                return newhead
                
        
# @lc code=end

