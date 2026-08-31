class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)

        for i in range(n - 1):
            need = target - numbers[i]
            lo, hi = i + 1, n - 1

            while lo <= hi:
                mid = (lo + hi) // 2
                if numbers[mid] == need:
                    return [i + 1, mid + 1]
                if numbers[mid] < need:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return []