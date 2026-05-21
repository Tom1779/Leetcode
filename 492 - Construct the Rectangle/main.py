class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area == 1:
            return [1,1]
        
        diff = 999999999999
        rect = [-1,-1]

        for i in range(1,int(area/2)+1):
            if area % i == 0:
                factor2 = int(area/i)
                if abs(factor2-i) < diff:
                    diff = abs(factor2-i)
                    if factor2 <= i:
                        rect[0] = i
                        rect[1] = factor2
                    else:
                        rect[0] = factor2
                        rect[1] = i

        return rect