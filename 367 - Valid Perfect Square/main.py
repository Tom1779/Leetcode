class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if math.sqrt(num).is_integer():
            return True

        return False