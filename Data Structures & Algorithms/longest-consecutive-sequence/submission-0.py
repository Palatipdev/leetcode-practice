class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set the sequence
        # loop the sequence, check for element - 1 if not found == start of sequence, search right until None then record the max

        seq = set(nums)
        res = 0
        for num in nums: #O(n)
            if num - 1 not in seq:
                curr = num
                count = 0
                while curr in seq: # O(k): k being length of sequence
                    count += 1
                    curr += 1

                res = max(res,count) 
        return res
        


