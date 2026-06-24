#
# @lc app=leetcode id=3700 lang=python
#
# [3700] Number of ZigZag Arrays II
#

# @lc code=start
class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7

        m = r - l + 1

        if n == 1:
            return m

        size = 2 * m

        # V2
        vec = [0] * size
        for i in range(m):
            vec[i] = i                  # up
            vec[m + i] = m - 1 - i     # down

        # Transition matrix
        M = [[0] * size for _ in range(size)]

        # up_new[i] = sum down[j], j < i
        for i in range(m):
            for j in range(i):
                M[i][m + j] = 1

        # down_new[i] = sum up[j], j > i
        for i in range(m):
            for j in range(i + 1, m):
                M[m + i][j] = 1

        def mat_mul(A, B):
            n1 = len(A)
            n2 = len(B)
            n3 = len(B[0])

            C = [[0] * n3 for _ in range(n1)]

            for i in range(n1):
                Ai = A[i]
                Ci = C[i]
                for k in range(n2):
                    if Ai[k] == 0:
                        continue
                    aik = Ai[k]
                    Bk = B[k]
                    for j in range(n3):
                        Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        def mat_vec_mul(A, v):
            n1 = len(A)
            res = [0] * n1
            for i in range(n1):
                s = 0
                row = A[i]
                for j in range(len(v)):
                    if row[j]:
                        s += row[j] * v[j]
                res[i] = s % MOD
            return res

        power = n - 2

        while power:
            if power & 1:
                vec = mat_vec_mul(M, vec)

            M = mat_mul(M, M)
            power >>= 1

        return sum(vec) % MOD
        
# @lc code=end

