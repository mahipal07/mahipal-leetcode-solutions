#
# @lc app=leetcode id=3471 lang=python3
#
# [3471] Find the Largest Almost Missing Integer
#
# 900/900 cases passed (5 ms)
# Your runtime beats 40.57 % of python3 submissions
# Your memory usage beats 75.41 % of python3 submissions (19.3 MB)

# @lc code=start
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = collections.defaultdict(int)
        n = len(nums)
        
        for i in range(n - k + 1):
            seen = set(nums[i:i + k])
            for num in seen:
                freq[num] += 1
                
        ans = -1
        for num, count in freq.items():
            if count == 1 and num > ans:
                ans = num
                
        return ans
        
# @lc code=end

