#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# 63/63 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 39.49 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

# @lc code=end

