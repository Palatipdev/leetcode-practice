from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = Counter()
        i = 0
        res = 0
        for j in range(len(s)):
            charCount[s[j]] += 1
            while ((j - i + 1 - max(charCount.values()))  > k):
                charCount[s[i]] -= 1
                i += 1
            currMax = j - i + 1
            if (currMax > res):
                res = currMax

        return res
            