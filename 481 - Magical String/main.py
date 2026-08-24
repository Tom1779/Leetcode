class Solution:
    def magicalString(self, n: int) -> int:
        if n < 4:
            return 1
        
        
        s = "122"

        cur_i = 3
        cur_num = "1"

        while(cur_i < n):
            s += int(s[cur_i-1]) * cur_num
            if cur_num == "1":
                cur_num = "2"
            else:
                cur_num = "1"
            cur_i += 1


        return s[0:n].count("1")