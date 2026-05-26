def get_area(cur_total, row, col, grid, visited):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
        return 0
    if grid[row][col] == 0 or (row,col) in visited:
        return 0
    else:
        visited.add((row,col))
        cur_total += get_area(0, row + 1, col, grid, visited)
        cur_total += get_area(0, row - 1, col, grid, visited)
        cur_total += get_area(0, row, col + 1, grid, visited)
        cur_total += get_area(0, row, col - 1, grid, visited)
        return cur_total + 1
        
        


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_a = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) in visited:
                    continue
                cur_a = get_area(0, row, col, grid, visited)
                if max_a < cur_a:
                    max_a = cur_a

        return max_a