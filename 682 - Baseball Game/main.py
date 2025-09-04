class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = []
        cur_ind = 0
        for op in operations:
            if op == "+":
                res.append(res[cur_ind-2] + res[cur_ind-1])
                cur_ind += 1
            elif op == "C":
                res.pop()
                cur_ind -= 1
            elif op == "D":
                res.append(res[cur_ind-1] * 2)
                cur_ind += 1
            else:
                res.append(int(op))
                cur_ind += 1
        return sum(res)