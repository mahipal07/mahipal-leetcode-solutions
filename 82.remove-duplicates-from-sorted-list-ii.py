#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# 167/167 cases passed (3 ms)
# Your runtime beats 27.89 % of python3 submissions
# Your memory usage beats 33.99 % of python3 submissions (19.4 MB)


# @lc code=start
# Definition for singly-linked list.                                                                   tion for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
            
        return dummy.next
# @lc code=end

