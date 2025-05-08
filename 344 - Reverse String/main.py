class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)/2):
            i_char = s[i]
            s[i] = s[-i-1]
            s[-i-1] = i_char