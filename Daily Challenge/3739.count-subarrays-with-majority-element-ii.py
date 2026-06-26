#
# @lc app=leetcode id=3739 lang=python
#
# [3739] Count Subarrays With Majority Element II
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
        # The prefix sum can range from -n to n. 
        # Shift everything by offset to keep indices positive.
        offset = n + 1
        bit = [0] * (2 * n + 2)
        
        def update(idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        # Insert the initial prefix sum P[0] = 0
        update(0 + offset, 1)
        
        ans = 0
        current_sum = 0
        
        for num in nums:
            current_sum += 1 if num == target else -1
            # Query for all previous prefix sums strictly less than current_sum
            ans += query(current_sum + offset - 1)
            # Add current prefix sum to the Fenwick tree
            update(current_sum + offset, 1)
            
        return ans
        
# @lc code=end

