class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        resNums = sorted(nums, reverse= True)
        return resNums[k - 1]