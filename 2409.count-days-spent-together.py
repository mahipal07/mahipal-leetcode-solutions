#
# @lc app=leetcode id=2409 lang=python3
#
# [2409] Count Days Spent Together
#
# 51/51 cases passed (0 ms)
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 47.08 % of python3 submissions (19.4 MB)

# @lc code=start
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def date_to_day(date: str) -> int:
            month, day = map(int, date.split('-'))
            return sum(days_in_month[:month - 1]) + day

        start = max(date_to_day(arriveAlice), date_to_day(arriveBob))
        end = min(date_to_day(leaveAlice), date_to_day(leaveBob))

        return max(0, end - start + 1)
    
# @lc code=end

