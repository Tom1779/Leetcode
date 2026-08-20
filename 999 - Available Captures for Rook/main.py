def findpawn(move, i, j, grid):
    if i > len(grid)-1 or i < 0 or j > len(grid[0])-1 or j < 0:
        return 0
    if grid[i][j] == "B":
        return 0
    if grid[i][j] == "p":
        return 1
    
    match move:
        case 'u':
            return findpawn(move, i-1, j, grid)
        case 'd':
            return findpawn(move, i+1, j, grid)
        case 'l':
            return findpawn(move, i, j-1, grid)
        case 'r':
            return findpawn(move, i, j+1, grid)




class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = (0,0)
        moves = ['u','d','l','r']
        total = 0

        found = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    rook = (i,j)
                    found = True
                    break
            if found:
                break

        for m in moves:
            total += findpawn(m, rook[0], rook[1], board)

        return total

        