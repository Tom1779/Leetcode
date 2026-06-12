class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points

        dist = dict()

        for p in points:
            if not (p[0],p[1]) in dist:
                dist[(p[0],p[1])] = [(p[0]-0)**2 + (p[1]-0)**2, 1]
            else:
                dist[(p[0],p[1])][1] += 1

        dist = dict(sorted(dist.items(), key=lambda item: item[1]))

        k_closest = []


        for key in dist:
            if dist[key][1] >= k:
                k_closest.extend([list(key)] * k)
                return k_closest

            k_closest.extend([list(key)] * dist[key][1])
            k -= dist[key][1]

