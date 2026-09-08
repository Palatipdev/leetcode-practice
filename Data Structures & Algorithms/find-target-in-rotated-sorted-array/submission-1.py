class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Binary search approach (haven't write it in awhile)

        lo = 0
        hi = len(nums) - 1
         
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target: return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            if nums[hi] >= nums[mid]:
                if nums[hi] >= target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1