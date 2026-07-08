#
# @lc app=leetcode id=3756 lang=python3
#
# [3756] Concatenate Non-Zero Digits and Multiply by Sum II
#

# @lc code=start

# 523/523 cases passed (550 ms)
# Your runtime beats 28.39 % of python3 submissions
# Your memory usage beats 45.68 % of python3 submissions (56.6 MB)

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        pref_sum = [0] * (n + 1)
        pref_nz_cnt = [0] * (n + 1)
        
        for i, ch in enumerate(s):
            val = int(ch)
            pref_sum[i + 1] = pref_sum[i] + val
            pref_nz_cnt[i + 1] = pref_nz_cnt[i] + (1 if val != 0 else 0)
            
        D = [int(ch) for ch in s if ch != '0']
        m = len(D)
        
        P = [0] * (m + 1)
        for i in range(m):
            P[i + 1] = (P[i] * 10 + D[i]) % MOD
            
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        ans = []
        for l, r in queries:
            total_sum = pref_sum[r + 1] - pref_sum[l]
            
            L_nz = pref_nz_cnt[l]
            R_nz = pref_nz_cnt[r + 1]
            
            if L_nz >= R_nz:
                ans.append(0)
            else:
                length = R_nz - L_nz
                x = (P[R_nz] - P[L_nz] * pow10[length]) % MOD
                ans.append((x * total_sum) % MOD)
                
        return ans
       
# @lc code=end

