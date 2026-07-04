#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
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
# 62/62 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 46.4 % of python3 submissions (20.3 MB)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        ptr = head
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        
        if count == k:
            reversed_head = self.reverseLinkedList(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return reversed_head
        return head

    def reverseLinkedList(self, head, k):
        new_head = None
        ptr = head
        while k > 0:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1
        return new_head
    
# @lc code=end

