class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 1:
            return []

        # for i in range(0, len(numbers) - 1):
        #     for j in range(i + 1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]

        # i, j = 0, 1
        # while i < len(numbers) - 1:
        #     while j < len(numbers) and numbers[j] < target:
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        #         else:
        #             j += 1
        #     i = i + 1
        #     j = i + 1

        i, j = 0, len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1

