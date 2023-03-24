class Solution:
    def mergeArrays(self, nums1, nums2):
        sum_dict = {}
        for pair in nums1:
            sum_dict[pair[0]] = pair[1]
            
        for pair in nums2:
            if not pair[0] in sum_dict.keys():
                sum_dict[pair[0]] = pair[1]
            else:
                sum_dict[pair[0]] += pair[1]
                
        num_sum = []
        for k,v in sum_dict.items():
            num_sum.append([k,v])
        
        num_sum.sort()
        return num_sum