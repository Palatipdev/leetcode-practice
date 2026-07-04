class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # nested loop approach
        result = [0] * (len(temperatures))
        for i in range(0,len(temperatures)):
            for j in range(i,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    result[i] = j - i
                    break
        return result