class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        max_dist = 0
        for i in range(len(colors)-1):
            for j in range(i+max_dist+1, len(colors)):
                if colors[i] != colors[j]:
                    max_dist = abs(i-j)

        return max_dist