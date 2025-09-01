class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        front = 0
        back = len(s)-1
        #iterating while the replace indexes do not overlap
        while front < back:
            #going until we find english alphabet character
            while(not s_list[front].isalpha()):
                front += 1
                #return existing string if overlap reached
                if front >= back:
                    return "".join(s_list)
            while(not s_list[back].isalpha()):
                back -= 1
                if front >= back:
                    return "".join(s_list)
            if front >= back:
                break
            temp = s_list[front]
            s_list[front] = s_list[back]
            s_list[back] = temp
            front += 1
            back -= 1
            continue
        return "".join(s_list)
