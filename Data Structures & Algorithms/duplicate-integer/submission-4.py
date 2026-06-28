class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = sorted(nums)
        for i in range(1,len(nums)):
            if(new[i - 1] == new[i]):
                return True
        return False