class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # remove all o that are surrounded
        # nested loop check o's adjacent field
        # how do we define the edge of the board?
        # so if o that is not at the edge have adjacent x on any side, that o = x
        ROWS, COLS = len(board), len(board[0])

        def bfs(r: int, c: int) -> None:
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == 'O':
                board[r][c] = 'T'
                bfs(r-1, c)
                bfs(r+1,c)
                bfs(r,c-1)
                bfs(r,c+1)

        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                    if board[i][j] == 'O' and ((i == 0 or i == len(board) - 1) or (j==0 or j == len(board[0]) -1)):
                        bfs(i, j)

        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        