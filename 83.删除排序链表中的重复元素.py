#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        newhead = head
        cur = head.next
        tail = head
        tail.next = None
        while cur:
            if cur.val == tail.val:
                cur = cur.next
            else:
                tail.next = cur
                tail = cur
                cur = cur.next
                tail.next = None
        return newhead
# @lc code=end

