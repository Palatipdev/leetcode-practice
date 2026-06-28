class Solution:
    def countBits(self, n: int) -> List[int]:
        listOut = []
        for i in range(0,n + 1):
            count = 0
            for char in bin(i):
                if char == "1":
                    count += 1;
            listOut.append(count)
        return listOut
