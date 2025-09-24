class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        #if there is one zero in the array our normal product will get messed up
        no_zero_product = 1
        num_of_zeros = 0
        for num in nums:
            if num == 0:
                num_of_zeros += 1
                #all products will be 0
                if num_of_zeros > 1:
                    return [0]*len(nums)
                product *= num
            else:
                product *= num
                no_zero_product *= num

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = no_zero_product
            else:
                nums[i]= int(product/nums[i])

        return nums
