#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head,tail):
            pre,cur = None,head
            while cur!=tail:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre
        
        if head == None or head.next==None:
            return head

        i = 0
        start,tail=head,head
        while i<k:
            if tail == None:
                return start
            tail=tail.next
            i+=1
        # 刚开始的[start,tail)
        newHead = reverse(start,tail)

        start.next = self.reverseKGroup(tail,k)
        return newHead


        



# @lc code=end

