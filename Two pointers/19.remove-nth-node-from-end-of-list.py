#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 208/208 cases passed (0 ms)
# Your runtime beats 100 % of python submissions
# Your memory usage beats 62.22 % of python submissions (12.3 MB)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        for _ in range(n):
            fast = fast.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next

        
# @lc code=end

