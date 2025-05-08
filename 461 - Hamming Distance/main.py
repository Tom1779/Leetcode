class Solution(object):
    def hammingDistance(self, x, y):
        x_bin = (bin(x)[2:])[::-1]
        y_bin = (bin(y)[2:])[::-1]

        ham = 0

        x_binL = len(x_bin)
        y_binL = len(y_bin)

        for i in range(max(x_binL, y_binL)):
            if (i > x_binL-1 and y_bin[i] == "1") or (i > y_binL-1 and x_bin[i] == "1"):
                ham += 1
                continue
            if i > x_binL-1 or i > y_binL-1:
                continue 
            if x_bin[i] != y_bin[i]:
                ham += 1

        return ham