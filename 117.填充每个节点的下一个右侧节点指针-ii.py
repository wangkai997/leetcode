#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def handle(last: 'Node' = None, p: 'Node' = None, nextStart: 'Node' = None):
            if last:
                last.next = p
            if nextStart == None:
                nextStart = p
            last = p
        

        if not root:
            return root
        start = root
        while start:
            last = Node(None)
            nextStart = Node(None)
            p = start
            while p:
                if p.left:
                    handle(last, p.left, nextStart)
                if p.right:
                    handle(last, p.right, nextStart)
                p = p.next
            start = nextStart
        return root



# @lc code=end

