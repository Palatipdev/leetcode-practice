class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in range(0,len(nums)):
            if (nums[i] in d):
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        reverse_dict = {v: k for k, v in d.items()}
        return reverse_dict[1]
        