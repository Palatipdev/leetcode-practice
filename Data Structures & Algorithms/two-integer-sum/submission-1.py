class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finalList = {}
        for i in range(0,len(nums)):
            if ((target - nums[i]) not in finalList):
                finalList[nums[i]] = i
            else:
                return [finalList[target-nums[i]], i]
        return finalList