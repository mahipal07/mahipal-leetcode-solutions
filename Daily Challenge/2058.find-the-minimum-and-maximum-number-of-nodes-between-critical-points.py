#
# @lc app=leetcode id=2058 lang=python3
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
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
# 139/139 cases passed (63 ms)
# Your runtime beats 93.9 % of python3 submissions
# Your memory usage beats 76.83 % of python3 submissions (62.9 MB)

class Solution:

  def nodesBetweenCriticalPoints(
      self, head: Optional[ListNode]
  ) -> List[int]:
    if not head or not head.next or not head.next.next:
      return [-1, -1]

    first_cp = -1
    last_cp = -1
    min_dist = float("inf")

    prev = head
    curr = head.next
    idx = 1

    while curr.next:
      if (curr.val > prev.val and curr.val > curr.next.val) or (
          curr.val < prev.val and curr.val < curr.next.val
      ):
        if first_cp == -1:
          first_cp = idx
        else:
          min_dist = min(min_dist, idx - last_cp)
        last_cp = idx

      prev = curr
      curr = curr.next
      idx += 1

    if first_cp == last_cp:
      return [-1, -1]

    return [min_dist, last_cp - first_cp]
  
# @lc code=end

