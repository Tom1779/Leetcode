class Solution:
    def countAndSay(self, n: int) -> str:
        string = "1"

        # Doing this since it doesnt work with later logic and its only the first case, allows us to start with a string if larger than 1
        if n == 1:
            return string

        for i in range(2, n+1):
            new_str = []
            cur_char = string[0]
            count = 0
            for char in string:
                if char == cur_char:
                    count += 1
                else:
                    new_str.append(f"{count}"+cur_char)
                    cur_char = char
                    count = 1
            new_str.append(f"{count}"+cur_char)
            string = "".join(new_str)
        return string