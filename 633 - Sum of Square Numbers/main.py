class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqr_c = math.sqrt(c)

        if sqr_c.is_integer():
            return True

        sqr_c = math.floor(sqr_c)

        squares = dict()

        for i in range(1,sqr_c+1):
            squares[i*i] = i

        for k in squares:
            if c - k in squares:
                return True

        return False