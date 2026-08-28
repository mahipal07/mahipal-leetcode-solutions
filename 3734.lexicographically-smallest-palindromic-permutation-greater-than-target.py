#
# @lc app=leetcode id=3734 lang=python3
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#
# 1035/1035 cases passed (23 ms)
# Your runtime beats 60.61 % of python3 submissions
# Your memory usage beats 48.48 % of python3 submissions (19.6 MB)

# @lc code=start
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        counts = Counter(s)
        
        odd_chars = [c for c, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = Counter({c: count // 2 for c, count in counts.items()})
        m = n // 2

        target_half_counts = Counter(target[:m])
        if all(target_half_counts[c] <= half_counts[c] for c in target_half_counts):
            if n % 2 == 1:
                if mid_char > target[m]:
                    return target[:m] + mid_char + target[:m][::-1]
                elif mid_char == target[m] and target[:m][::-1] > target[m + 1:]:
                    return target[:m] + mid_char + target[:m][::-1]
            else:
                if target[:m][::-1] > target[m:]:
                    return target[:m] + target[:m][::-1]

        prefix_counts = Counter(target[:m])
        for i in range(m - 1, -1, -1):
            prefix_counts[target[i]] -= 1
            if prefix_counts[target[i]] == 0:
                del prefix_counts[target[i]]

            if all(prefix_counts[c] <= half_counts[c] for c in prefix_counts):
                rem_counts = half_counts - prefix_counts
                for o in range(ord(target[i]) + 1, ord('z') + 1):
                    char = chr(o)
                    if rem_counts[char] > 0:
                        rem_counts[char] -= 1
                        suffix = "".join(sorted(rem_counts.elements()))
                        first_half = target[:i] + char + suffix
                        return first_half + mid_char + first_half[::-1]

        return ""
      
# @lc code=end

