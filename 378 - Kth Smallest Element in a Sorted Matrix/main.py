class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        elements = dict()
        for i in range(min(len(matrix), k)):
            for j in range(min(len(matrix), k)):
                if not matrix[i][j] in elements:
                    elements[matrix[i][j]] = 1
                else:
                    elements[matrix[i][j]] += 1
        
        elements = dict(sorted(elements.items()))
        
        for key,v in elements.items():
            k -= v
            if k <= 0:
                return key