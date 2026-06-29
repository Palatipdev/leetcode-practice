class Solution:
    def isHappy(self, n: int) -> bool:
        existedList = []
        while(n != 1):
            sum = 0
            if (n in existedList):
                return False
            else:
                existedList.append(n)
                for digit in str(n):
                    sum += int(digit) * int(digit)
            n = sum

        return True
            
        