class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack approach
        result = [0] * (len(temperatures))
        stack = []
        stack.append(0)
        for i in range(1,len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                    j = stack.pop()
                    result[j] = i - j           
            stack.append(i)
        return result