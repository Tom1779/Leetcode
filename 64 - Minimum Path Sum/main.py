def get_sum(grid, row, col, mp):
    if row == len(grid)-1 and col == len(grid[0])-1:
        return grid[row][col]

    if (row,col) in mp:
        return mp[(row,col)]

    down = 99999999999
    right = 99999999999
        
    if row < len(grid)-1:
        down = get_sum(grid, row+1, col, mp)
    if col < len(grid[0])-1:
        right = get_sum(grid, row, col+1, mp)

    mp[(row,col)] = grid[row][col]+min(down,right)

    return mp[(row,col)]
    

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
            
        return get_sum(grid, 0, 0, {})