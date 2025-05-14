class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        digit_count = 0
        letter_count = 0
        digits = []
        letters = []

        for c in s:
            if ord(c) <= 57:
                digit_count += 1
                digits.append(c)
            else:
                letter_count += 1
                letters.append(c)
            
        if abs(digit_count - letter_count) > 1:
            return ""

        if letter_count > digit_count:
            new_string = [l + d for l,d in zip(letters,digits)] + [letters[-1]]

        elif digit_count > letter_count:
            new_string = [d + l for d,l in zip(digits,letters)] + [digits[-1]]
        
        else:
            new_string = [d + l for d,l in zip(digits,letters)]

        return "".join(new_string)