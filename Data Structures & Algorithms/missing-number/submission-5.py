class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        j = 0
        nums.sort()
        for i in range(0,len(nums)):
            if (j != nums[i]):
                return j
            else:
                j += 1
        return len(nums)
