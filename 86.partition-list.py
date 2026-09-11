#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# 169/169 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 77.23 % of python3 submissions (19.3 MB)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        less = less_head
        greater = greater_head
        
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
            
        greater.next = None
        less.next = greater_head.next
        
        return less_head.next
    
# @lc code=end

