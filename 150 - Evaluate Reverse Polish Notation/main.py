class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #creating a number stack since operations in polish notation are dont on the last 2 numbers
        nums = []
        for token in tokens:
            if token == '+':
                val = nums[-2] + nums[-1]
                # removing operands and adding result to be used for next operation
                nums.pop()
                nums.pop()
                nums.append(val)
            elif token == '-':
                val = nums[-2] - nums[-1]
                nums.pop()
                nums.pop()
                nums.append(val)
            elif token == '*':
                val = nums[-2] * nums[-1]
                nums.pop()
                nums.pop()
                nums.append(val)
            elif token == '/':
                val = int(nums[-2] / nums[-1])
                nums.pop()
                nums.pop()
                nums.append(val)
            else:
                nums.append(int(token))
                
        #after all the operations our stack should just contain the result
        return nums[0]