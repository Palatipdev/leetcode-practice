class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = {}

        for i in range (0,len(position)):
            pos_speed[position[i]] = speed[i]
        tuple_sorted = sorted(pos_speed.items() , key=lambda x: x[0])

        stack = []
        for i in range (len(tuple_sorted) - 1 , -1, -1):
            arrivalTimeCurr = (target - tuple_sorted[i][0]) / tuple_sorted[i][1]
            if stack and arrivalTimeCurr > stack[-1]:
                stack.append(arrivalTimeCurr)
            if not stack:
                stack.append(arrivalTimeCurr)
        return len(stack)