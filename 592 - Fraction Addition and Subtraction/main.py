import re
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        parts = re.split(r'([+-])', expression)

        if parts[0] == "":
            parts.pop(0)

        if parts[0] != "-":
            parts.insert(0, "+")

        total = 0
        index = 0

        while(index < len(parts)):
            num, den = parts[index+1].split('/')
            frac = Fraction(int(num), int(den))
            if parts[index] == "+":
                total += frac
            else:
                total -= frac
            index += 2

        return str(total.numerator) + "/" + str(total.denominator)