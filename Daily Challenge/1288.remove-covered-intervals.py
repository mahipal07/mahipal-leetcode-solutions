#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#
# 34/34 cases passed (4 ms)
# Your runtime beats 46.19 % of python3 submissions
# Your memory usage beats 47.88 % of python3 submissions (19.6 MB)

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        prev_end = 0
        
        for _, end in intervals:
            if end > prev_end:
                count += 1  
                prev_end = end
                
        return count


# @lc code=end

