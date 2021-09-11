#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre= None
        slow = head
        fast = head
        i = 0
        while fast:
            if i<n:
                fast = fast.next
                i+=1
            else:
                fast = fast.next
                pre = slow
                slow = slow.next 
        if slow == head:
            return head.next
        pre.next = slow.next
        return head
        
# @lc code=end

