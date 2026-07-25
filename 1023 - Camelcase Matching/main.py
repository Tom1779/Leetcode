class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        cm = []

        for query in queries:
            valid = True
            i = 0
            for char in query:
                if char.isupper() and i == len(pattern):
                    valid =  False
                    break
                if char.isupper() and char != pattern[i]:
                    valid = False
                    break
                if  i < len(pattern) and char == pattern[i]:
                    i += 1
            if i < len(pattern):
                valid = False
            cm.append(valid)

        return cm

            

                