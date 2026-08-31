from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        freshFruitCount = 0

        
        def addCell(r: int , c:int, freshFruitCount: int ) -> int:
            if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or  grid[r][c] == 0 or grid[r][c] == 2:
                return freshFruitCount
            q.append((r, c))
            grid[r][c] = 2
            freshFruitCount -= 1
            return freshFruitCount

        for i in range(0,ROWS):
            for j in range (0, COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    freshFruitCount += 1
        if freshFruitCount == 0:
            return 0
        
        minutes = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                freshFruitCount = addCell(r - 1, c, freshFruitCount)
                freshFruitCount = addCell(r + 1, c, freshFruitCount)
                freshFruitCount = addCell(r, c - 1, freshFruitCount)
                freshFruitCount = addCell(r, c + 1, freshFruitCount)

            minutes += 1
        
        if (freshFruitCount == 0):
            return minutes
        else:
            return -1