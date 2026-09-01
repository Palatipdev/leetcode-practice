class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentChar = set()
        leftPointer = 0
        res = 0

        for rightPointer in range(len(s)):
            while s[rightPointer] in currentChar:
                currentChar.remove(s[leftPointer])
                leftPointer += 1
            currentChar.add(s[rightPointer])
            currMax = rightPointer - leftPointer + 1
            if (currMax > res):
                res = currMax
        return res
            