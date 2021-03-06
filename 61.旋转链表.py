#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k==0 or not head or not head.next:
            return head
        n = 1
        cur = head
        while cur.next:
            n+=1
            cur = cur.next
        
        if k%n==0:
            return head
        cur.next = head
        
        pre,cur = cur,head
        i = 0
        while n-k%n!=i:
            i = i+1
            pre = cur
            cur = cur.next
        pre.next = None
        return cur        

# @lc code=end

