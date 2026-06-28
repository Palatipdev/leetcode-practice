class Solution:
    def countBits(self, n: int) -> List[int]:
        listOut = []
        listOut.append(0)
        for i in range(1,n + 1):
            listOut.append(listOut[i >> 1] + (i & 1))
        return listOut
        