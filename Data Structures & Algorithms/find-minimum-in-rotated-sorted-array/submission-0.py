class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        lo = 0
        hi = len(nums) - 1
        minVal = float("inf")

        while lo <= hi:
            mid = (lo + hi) // 2
            print(f"lo: {lo}")
            print(f"mid: {mid}")
            print(f"hi: {hi}")
            if nums[lo] <= nums[mid]:
                if nums[lo] < minVal:
                    minVal = nums[lo]
                lo = mid + 1
            else:
                if nums[mid] < minVal:
                    minVal = nums[mid]
                hi = mid - 1
        return minVal