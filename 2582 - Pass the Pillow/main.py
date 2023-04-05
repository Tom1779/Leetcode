class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p = n-1
        rotation = int(time/p)
        
        if rotation % 2 == 0:
            if time%p == 0:
                return 1
            else:
                return time%p + 1
        
        if time%p == 0:
                return n
        else:
            return n - time%p