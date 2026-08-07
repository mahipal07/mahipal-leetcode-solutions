#
# @lc app=leetcode id=3348 lang=python3
#
# [3348] Smallest Divisible Digit Product II
#
# 954/954 cases passed (877 ms)
# Your runtime beats 38.46 % of python3 submissions
# Your memory usage beats 25.64 % of python3 submissions (51.8 MB)

# @lc code=start
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp_t = t
        c2 = c3 = c5 = c7 = 0

        while temp_t % 2 == 0:
            temp_t //= 2
            c2 += 1
        while temp_t % 3 == 0:
            temp_t //= 3
            c3 += 1
        while temp_t % 5 == 0:
            temp_t //= 5
            c5 += 1
        while temp_t % 7 == 0:
            temp_t //= 7
            c7 += 1

        if temp_t > 1:
            return "-1"

        factor_counts = [
            [0, 0, 0, 0],  # 0
            [0, 0, 0, 0],  # 1
            [1, 0, 0, 0],  # 2
            [0, 1, 0, 0],  # 3
            [2, 0, 0, 0],  # 4
            [0, 0, 1, 0],  # 5
            [1, 1, 0, 0],  # 6
            [0, 0, 0, 1],  # 7
            [3, 0, 0, 0],  # 8
            [0, 2, 0, 0],  # 9
        ]

        def get_min_digits(r2, r3, r5, r7):
            r2 = max(0, r2)
            r3 = max(0, r3)
            r5 = max(0, r5)
            r7 = max(0, r7)

            best = ""
            min_len = float("inf")

            for d2 in range(3):
                for d3 in range(2):
                    for d4 in range(2):
                        for d6 in range(2):
                            rem2 = r2 - d2 - 2 * d4 - d6
                            rem3 = r3 - d3 - d6

                            d8 = (rem2 + 2) // 3 if rem2 > 0 else 0
                            d9 = (rem3 + 1) // 2 if rem3 > 0 else 0

                            total_len = (
                                d2 + d3 + d4 + d6 + d8 + d9 + r5 + r7
                            )

                            cur = (
                                "2" * d2
                                + "3" * d3
                                + "4" * d4
                                + "5" * r5
                                + "6" * d6
                                + "7" * r7
                                + "8" * d8
                                + "9" * d9
                            )

                            if total_len < min_len or (
                                total_len == min_len and (best == "" or cur < best)
                            ):
                                min_len = total_len
                                best = cur

            return best

        n = len(num)

        first_zero = -1
        for i, ch in enumerate(num):
            if ch == "0":
                first_zero = i
                break

        if first_zero != -1:
            num = (
                num[:first_zero]
                + "1"
                + "1" * (n - first_zero - 1)
            )

        pref2 = [0] * (n + 1)
        pref3 = [0] * (n + 1)
        pref5 = [0] * (n + 1)
        pref7 = [0] * (n + 1)

        for i in range(n):
            d = int(num[i])
            pref2[i + 1] = pref2[i] + factor_counts[d][0]
            pref3[i + 1] = pref3[i] + factor_counts[d][1]
            pref5[i + 1] = pref5[i] + factor_counts[d][2]
            pref7[i + 1] = pref7[i] + factor_counts[d][3]

        if first_zero == -1:
            min_suffix = get_min_digits(
                c2 - pref2[n],
                c3 - pref3[n],
                c5 - pref5[n],
                c7 - pref7[n],
            )
            if min_suffix == "":
                return num

        for i in range(n - 1, -1, -1):
            start_d = int(num[i]) + 1

            if first_zero != -1 and i > first_zero:
                continue

            if first_zero != -1 and i == first_zero:
                start_d = 1

            for d in range(start_d, 10):
                rem2 = c2 - pref2[i] - factor_counts[d][0]
                rem3 = c3 - pref3[i] - factor_counts[d][1]
                rem5 = c5 - pref5[i] - factor_counts[d][2]
                rem7 = c7 - pref7[i] - factor_counts[d][3]

                min_suffix = get_min_digits(rem2, rem3, rem5, rem7)

                len_needed = len(min_suffix)
                available_len = n - 1 - i

                if len_needed <= available_len:
                    return (
                        num[:i]
                        + str(d)
                        + "1" * (available_len - len_needed)
                        + min_suffix
                    )

        target_len = n + 1
        while True:
            min_suffix = get_min_digits(c2, c3, c5, c7)
            if len(min_suffix) <= target_len:
                return (
                    "1" * (target_len - len(min_suffix))
                    + min_suffix
                )
            target_len += 1

# @lc code=end

