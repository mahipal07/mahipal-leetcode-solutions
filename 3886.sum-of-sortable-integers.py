#
# @lc app=leetcode id=3886 lang=python3
#
# [3886] Sum of Sortable Integers
#
# 1054/1054 cases passed (2080 ms)
# Your runtime beats 51.35 % of python3 submissions
# Your memory usage beats 78.33 % of python3 submissions (31.3 MB)

# @lc code=start
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        def check(k: int) -> bool:
            prev_max = float("-inf")
            for i in range(0, n, k):
                drops = 0
                drop_idx = -1
                for j in range(k):
                    if nums[i + j] > nums[i + (j + 1) % k]:
                        drops += 1
                        drop_idx = j
                if drops > 1:
                    return False

                if drops == 0:
                    b_min = nums[i]
                    b_max = nums[i]
                else:
                    b_min = nums[i + (drop_idx + 1) % k]
                    b_max = nums[i + drop_idx]

                if prev_max > b_min:
                    return False
                prev_max = b_max

            return True

        for k in range(1, n + 1):
            if n % k == 0 and check(k):
                ans += k

        return ans
        
# @lc code=end

