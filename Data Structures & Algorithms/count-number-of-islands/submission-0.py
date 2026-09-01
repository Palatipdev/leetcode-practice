from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        
        def dfs(r:int , c: int):
            if (r > ROWS -1 or r < 0 or c > COLS -1 or c < 0 or grid[r][c] == "0" or (r, c)  in visited):
                return
            visited.add((r , c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i,j)
                    res += 1

        return res
              
                
