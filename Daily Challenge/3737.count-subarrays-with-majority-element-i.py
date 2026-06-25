#
# @lc app=leetcode id=3737 lang=python
#
# [3737] Count Subarrays With Majority Element I
#

# @lc code=start
class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        size = 2 * n + 5
        bit = [0] * size

        def update(i, delta):
            while i < size:
                bit[i] += delta
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        offset = n + 2

        prefix = 0
        ans = 0

        # empty prefix
        update(offset, 1)

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            idx = prefix + offset

            # previous prefix sums < current prefix sum
            ans += query(idx - 1)

            update(idx, 1)

        return ans
        
# @lc code=end

