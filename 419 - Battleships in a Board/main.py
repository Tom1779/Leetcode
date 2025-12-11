class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        battleships = 0

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'X':
                    visited.add((row,col))
                    if row > 0:
                        if (row-1,col) in visited:
                            continue
                    if col > 0:
                        if (row,col-1) in visited:
                            continue
                    battleships += 1
        return battleships