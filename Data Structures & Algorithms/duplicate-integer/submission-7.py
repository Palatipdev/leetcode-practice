class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        meow = []
        for num in nums:
            if num in meow:
                return True
            else:
                meow.append(num)
        return False