#
# @lc app=leetcode id=2948 lang=python3
#
# [2948] Make Lexicographically Smallest Array by Swapping Elements
#
# 523/523 cases passed (196 ms)
# Your runtime beats 99.25 % of python3 submissions
# Your memory usage beats 49.62 % of python3 submissions (48.9 MB)

# @lc code=start
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        
        groups = []
        num_to_group = {}
        
        for num in sorted_nums:
            if not groups or num - groups[-1][-1] > limit:
                groups.append([num])
            else:
                groups[-1].append(num)
            num_to_group[num] = len(groups) - 1
            
        group_ptrs = [0] * len(groups)
        result = []
        
        for num in nums:
            grp_idx = num_to_group[num]
            result.append(groups[grp_idx][group_ptrs[grp_idx]])
            group_ptrs[grp_idx] += 1
            
        return result
            
# @lc code=end

