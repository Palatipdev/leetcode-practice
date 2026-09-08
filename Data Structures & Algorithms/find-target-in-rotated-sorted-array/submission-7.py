class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # so the trivial approach is just brute forcing checking each element using a for loop one by one which is linear
        # the faster approach which is O(log n) time is using binary search. 
        # we can do this by first calculating mid as normal, and we check which side , lo to mid  / mid to hi either of them are sorted, 
        # because we know they are sorted, we can be sure to check if that side has a target in range between lower and higher bound i.e. nums[lo] to nums[mid - 1] or nums[mid + 1] to nums[hi]
        #if the target is in that range then we can run a normal binary search on that range
        # otherwise we would completely disregard that range and run the same process on the other half

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            print(lo)
            print(mid)
            print(hi)
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[hi] >= target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1