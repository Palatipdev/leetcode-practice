import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        result = -1 
        heapq.heapify(nums)
        while len(nums) > k:
            result = heapq.heappop(nums)
        
        return nums[0]