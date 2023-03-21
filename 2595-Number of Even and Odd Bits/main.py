class Solution:
    def evenOddBit(self, n: int):
        bits = [0,0]
        str_n = bin(n)[2:][::-1]
        for dig in range(len(str_n)):
            if str_n[dig] == "1":
                if dig % 2 == 0:
                    bits[0] += 1
                else:
                    bits[1] += 1
                    
        return bits