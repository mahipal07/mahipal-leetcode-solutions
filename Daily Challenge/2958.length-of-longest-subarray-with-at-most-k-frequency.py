#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#
# 994/994 cases passed (350 ms)
# Your runtime beats 5.19 % of python3 submissions
# Your memory usage beats 72.85 % of python3 submissions (35.2 MB)

# @lc code=start
from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = Counter()
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            count[nums[right]] += 1
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            
        return max_len
     
# @lc code=end

