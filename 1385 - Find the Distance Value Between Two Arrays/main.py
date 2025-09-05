class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        for item1 in arr1:
            for item2 in arr2:
                if abs(item1-item2) <= d:
                    #Basically negates the increment after exiting this loop
                    count -= 1
                    break
            count += 1

        return count