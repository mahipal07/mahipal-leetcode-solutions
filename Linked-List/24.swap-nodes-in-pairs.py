#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 55/55 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 22.12 % of python3 submissions (19.3 MB)

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            
            first.next = second.next
            second.next = first
            current.next = second
            
            current = first
            
        return dummy.next
# @lc code=end

