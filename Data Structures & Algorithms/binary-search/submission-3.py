class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        upper = len(nums) - 1
        lower = 0
        found = False
        while (found == False and upper >= lower):
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lower = mid + 1
                mid = lower + (upper - lower) // 2
            else:
                upper = mid - 1
                mid = lower + (upper - lower) // 2
        return -1