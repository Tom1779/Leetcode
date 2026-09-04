class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        largeInteger = list(reversed(list(digits)))
        for digit in range(len(largeInteger)):
            if not largeInteger[digit] == 9:
                largeInteger[digit] += 1
                break
            else:
                largeInteger[digit] = 0
                if digit == len(largeInteger) - 1:
                    largeInteger.append(1)
                    break
                
        return reversed(largeInteger)