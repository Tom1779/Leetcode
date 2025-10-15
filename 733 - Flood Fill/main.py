def change_adjacent(image, row, col, color, new_color, visited):
    if image[row][col] != color or [row,col] in visited:
        return
    #to avoid infinite loop
    visited.append([row,col])
    image[row][col] = new_color
    if row != 0:
        change_adjacent(image, row-1, col, color, new_color, visited)
    if row != len(image)-1:
        change_adjacent(image, row+1, col, color, new_color, visited)
    if col != 0:
        change_adjacent(image, row, col-1, color, new_color, visited)
    if col != len(image[row])-1:
        change_adjacent(image, row, col+1, color, new_color, visited)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = []
        change_adjacent(image,sr,sc,image[sr][sc],color,visited)

        return image