class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # volume = (right - left) * (min(heights[right],heights[left]))
        # plan: two pointers

        i, j = 0, len(heights) - 1
        res = 0

        while j > i:
            # move i: when heights of i + 1 is greater than i
            # move j: when heights of j - 1 is greater than j
            # but it can't just be simply greater than
            # actually reading the example graph it is like that
            res = max(res, (j - i) * (min(heights[j], heights[i])))
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return res
