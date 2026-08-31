class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = []
        
        def addCell(r: int, c:int):
            if (r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or grid[r][c] == -1 or (r, c) in visited):
                return 
            q.append([r, c])
            visited.add((r, c))

        for i in range(0,ROWS):
            for j in range(0,COLS):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.pop(0)
                grid[r][c] = dist
                visited.add((r, c))
                addCell(r-1,c)
                addCell(r+1,c)
                addCell(r,c-1)
                addCell(r,c+1)

            dist += 1