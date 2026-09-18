#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# 44/44 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 65.51 % of python3 submissions (19.4 MB)

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
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
            
        curr = prev.next
        
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
            
        return dummy.next
    
# @lc code=end

