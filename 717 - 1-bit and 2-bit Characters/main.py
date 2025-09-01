class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if bits[-1] == 0:
            #only 1 number and list so can only be 0
            if len(bits) == 1:
                return True
            num_of_ones = 0
            index = -2
            while(bits[index] != 0):
                num_of_ones += 1
                index -= 1
                #making sure we do not exceed the array range
                if abs(index) > len(bits):
                    break
            #if the amount of one preceeding 0 is even that means they each represent a 2 bit character and the 0 must be the start of a new sequenece
            if num_of_ones % 2 == 0:
                return True
        return False