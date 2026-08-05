class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        pv = []

        for i in range(lo,hi+1):
            num = i
            ops = 0
            while(num != 1):
                if num % 2 == 0:
                    num = num/2
                else:
                    num = num*3+1
                ops+=1
            pv.append((i, ops))

        pv.sort(key=lambda x: x[1])

        return pv[k-1][0]