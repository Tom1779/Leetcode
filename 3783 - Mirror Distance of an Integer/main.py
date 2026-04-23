class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 0
        rev_n = 0
        temp_n = n

        while temp_n>0:
            digit = temp_n%10
            rev_n = (rev_n * 10) + digit
            temp_n = floor(temp_n/10)

        return int(abs(n-rev_n))