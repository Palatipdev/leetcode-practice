class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        print(self.nums)
        self.nums.append(val)
        print(self.nums)
        self.nums.sort(reverse=True)

        return self.nums[self.k - 1]