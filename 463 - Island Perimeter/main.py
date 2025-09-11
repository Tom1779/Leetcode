class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        per = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    per += 4
                    if i - 1 >= 0:
                        if grid[i-1][j] == 1:
                            per -= 1
                    if i + 1 <= len(grid) - 1:
                        if grid[i+1][j] == 1:
                            per -= 1
                    if j - 1 >= 0:
                        if grid[i][j-1] == 1:
                            per -= 1
                    if j + 1 <= len(grid[i]) - 1:
                        if grid[i][j+1] == 1:
                            per -= 1

        return per