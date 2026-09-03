import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heappush
        # heappop
        # heapify
        myDict = Counter(nums)
        heap = []

        for (key, val) in myDict.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for i in range(len(heap)):
            result.append(heap[i][1])
        return result