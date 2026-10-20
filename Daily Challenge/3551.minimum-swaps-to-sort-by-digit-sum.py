#
# @lc app=leetcode id=3551 lang=python3
#
# [3551] Minimum Swaps to Sort by Digit Sum
#
# 807/807 cases passed (983 ms)
# Your runtime beats 85.67 % of python3 submissions
# Your memory usage beats 48.33 % of python3 submissions (48.1 MB)

# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n: int) -> int:
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {val: i for i, val in enumerate(sorted_nums)}

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or pos[nums[i]] == i:
                continue

            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = pos[nums[curr]]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps
        
# @lc code=end

