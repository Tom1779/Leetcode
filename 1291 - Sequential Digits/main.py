class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sd = []

        num = ""

        for i in range(1,len(str(low))+1):
            num += str(i)

        multiple = len(num)
        lead = 1

        while(int(num) <= high):
            if int(num) >= low:
                sd.append(int(num))
            if num[-1] == "9":
                multiple += 1
                lead = 1
                num = ""
            else:
                num = ""
                lead += 1
            for i in range(lead,lead+multiple):
                    num += str(i)
            

        return sd
