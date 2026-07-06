class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # remove all o that are surrounded
        # nested loop check o's adjacent field
        # how do we define the edge of the board?
        # so if o that is not at the edge have adjacent x on any side, that o = x
        safe = []


        def bfs(i: int, j: int) -> None:
            queue = [[i,j]]
            while queue:
                r, c = queue.pop(0)
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and [r, c] not in safe:
                    safe.append([r, c])
                    if r-1 >= 0 and board[r-1][c] == 'O':
                        queue.append([r-1, c])
                    if r+1 < len(board) and board[r+1][c] == 'O':
                        queue.append([r+1, c])
                    if c-1 >= 0 and board[r][c-1] == 'O':
                        queue.append([r, c-1])                        
                    if c+1 < len(board[0]) and board[r][c+1] == 'O':
                        queue.append([r, c+1])

        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                    if board[i][j] == 'O' and ((i == 0 or i == len(board) - 1) or (j==0 or j == len(board[0]) -1)):
                        bfs(i, j)

        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == 'O' and [i,j] not in safe:
                    board[i][j] = 'X'
        