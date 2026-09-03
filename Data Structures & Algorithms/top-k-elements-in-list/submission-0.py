from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = Counter(nums)

        keys = sorted(numDict, key=numDict.get, reverse = True)
        return keys[:k]