#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode((l1.val+l2.val)%10)
        p = head
        # add 表示进位
        add = (l1.val + l2.val) // 10
        while l1.next != None or l2.next != None:
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            value = l1.val + l2.val + add
            p.next = ListNode(value % 10)
            add = value // 10
            p = p.next
        if add == 1:
            p.next = ListNode(1) 
        return head
        # head = ListNode(l1.val + l2.val)
        # cur = head
        # while l1.next or l2.next:
        #     l1 = l1.next if l1.next else ListNode()
        #     l2 = l2.next if l2.next else ListNode()
        #     cur.next = ListNode(l1.val + l2.val + cur.val // 10)
        #     cur.val = cur.val % 10
        #     cur = cur.next
        # if cur.val >= 10:
        #     cur.next = ListNode(cur.val // 10)
        #     cur.val = cur.val % 10
        # return head
# @lc code=end

