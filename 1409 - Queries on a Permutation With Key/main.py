class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1,m+1)]
        pq = []

        for q in queries:
            pq.append(p.index(q))
            p.pop(pq[-1])
            p.insert(0,q)

        return pq