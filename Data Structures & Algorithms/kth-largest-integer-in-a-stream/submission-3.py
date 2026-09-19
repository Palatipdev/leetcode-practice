import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        garbage = 0
        while len(self.heap) > self.k:
            garbage = heapq.heappop(self.heap)

        return self.heap[0]