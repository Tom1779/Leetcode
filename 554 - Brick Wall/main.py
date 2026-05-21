class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        max_break = 0
        breaks = {}
        for w in wall:
            cur = 0
            for b in range(len(w)-1):
                cur += w[b]
                if not cur in breaks:
                    breaks[cur] = 1
                else:
                    breaks[cur] += 1
                if breaks[cur] > max_break:
                    max_break = breaks[cur]

        return len(wall)-max_break
