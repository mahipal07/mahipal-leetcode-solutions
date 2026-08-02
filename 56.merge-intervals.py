#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# 172/172 cases passed (7 ms)
# Your runtime beats 71.71 % of python3 submissions
# Your memory usage beats 71.15 % of python3 submissions (22.4 MB)

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_merged_start, last_merged_end = merged[-1]

            if current_start <= last_merged_end:
                # Merge them by updating the end time of the last merged interval
                merged[-1][1] = max(last_merged_end, current_end)
            else:
                # No overlap, add the current interval to the list
                merged.append(intervals[i])

        return merged
    
# @lc code=end

