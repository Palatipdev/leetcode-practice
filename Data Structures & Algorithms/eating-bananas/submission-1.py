import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # base case: F[0] = 0
        # recurrence: F[k + 1] = min(F[k + 1] + piles[i], F[k])
        # Time complexity: O(n)

        def checkValid(k):
            hourTaken = 0
            for pile in piles:             
                hourTaken += math.ceil(pile / k)
            return hourTaken <= h

        lo = 1
        hi = max(piles)

        while lo <= hi:
            print(lo)
            print(hi)
            mid = (lo + hi) // 2
            if checkValid(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        print(lo)
        print(hi)
        return lo
        
        
        
