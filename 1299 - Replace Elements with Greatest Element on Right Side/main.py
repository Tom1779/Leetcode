class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = arr[-1]
        arr[-1] = -1

        for i in range(2,len(arr)+1):
            temp = arr[-i]
            arr[-i] = max_element

            if temp > max_element:
                max_element = temp

        return arr
