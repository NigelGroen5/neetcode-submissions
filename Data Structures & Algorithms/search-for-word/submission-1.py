class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # don't wanna revisit same position twice in path

        # r=row, c=col, i =curr char in target word looking for
        def dfs(r, c, i):
            if i == len(word): # finished word
                return True
            # if go out of bounds of board
            if (r < 0 or c < 0 or 
                r >= ROWS or c>= COLS or 
                word[i] != board[r][c] or # doesn't match
                (r,c) in path): # not already visited 
                return False
            #now no found char looking for 
            path.add((r,c))
            # run dfs in all 4 adjacent positions
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            path.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): 
                    return True
        return False

