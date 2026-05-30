class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {c:0 for c in order}

        for c in s:
            if c in order_dict:
                order_dict[c] += 1
            else:
                order_dict[c] = 1

        sort_s = ""

        for k,v in order_dict.items():
            sort_s += k*(v)

        return sort_s 