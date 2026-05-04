class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotated = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if not j in rotated.keys():
                    rotated[j] = [matrix[i][j]]
                else:
                    rotated[j].insert(0, matrix[i][j])

        for i in range(len(matrix)):
            matrix[i] = rotated[i]

        return