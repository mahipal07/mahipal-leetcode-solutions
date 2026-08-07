#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# 232/232 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 39.75 % of python3 submissions (19.4 MB)

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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Compute the length of the list and find the tail
        last_node = head
        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1
            
        # 2. Adjust k in case k >= length
        k = k % length
        if k == 0:
            return head
            
        # 3. Connect tail to head to make it circular
        last_node.next = head
        
        # 4. Find the new tail: (length - k - 1) steps from head
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        # 5. The new head is the node after the new tail
        new_head = new_tail.next
        
        # 6. Break the circular connection
        new_tail.next = None
        
        return new_head
   
# @lc code=end

