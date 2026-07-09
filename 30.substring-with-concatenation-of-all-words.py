#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# 182/182 cases passed (23 ms)
# Your runtime beats 77.05 % of python3 submissions
# Your memory usage beats 97.55 % of python3 submissions (19.7 MB)

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        results = []

        # Build the initial frequency map using a standard dictionary
        word_freq = {}
        for w in words:
            word_freq[w] = word_freq.get(w, 0) + 1

        # We slide over the string in offsets of word_len to cover all possibilities
        for i in range(word_len):
            left = i
            right = i
            curr_freq = {}
            count = 0

            while right + word_len <= len(s):
                # Extract the word from the current right position
                word = s[right:right + word_len]
                right += word_len

                if word in word_freq:
                    curr_freq[word] = curr_freq.get(word, 0) + 1
                    count += 1

                    # If we have more of 'word' than allowed, slide 'left' forward
                    while curr_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        curr_freq[left_word] -= 1
                        count -= 1
                        left += word_len

                    # If the number of words matches, we found a valid index
                    if count == word_count:
                        results.append(left)
                else:
                    # If word is not in words list, reset the window
                    curr_freq = {}
                    count = 0
                    left = right

        return results 
# @lc code=end

