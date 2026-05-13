def isolate_numbers(num):
    first = num[0]
    index = 0
    for char in range(1,len(num)):
        if(num[char] != "+"):
            first += num[char]
        else:
            index = char
            break
    index += 1
    second = ""
    if num[index] == "-":
        second = "-"
        index += 1
    third = num[index]  
    for char in range(index+1,len(num)-1):
        third += num[char]

    return [first, second, third]



class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        num1_str = isolate_numbers(num1)
        num2_str = isolate_numbers(num2)

        num1_int1 = int("".join(map(str, num1_str[0])))
        num1_int2 = int("".join(map(str, num1_str[2])))
        if num1_str[1] == "-":
            num1_int2 *= -1

        num2_int1 = int("".join(map(str, num2_str[0])))
        num2_int2 = int("".join(map(str, num2_str[2])))
        if num2_str[1] == "-":
            num2_int2 *= -1

        prod1 = num1_int1 * num2_int1
        
        prod2 = num1_int2 * num2_int2 * -1

        prod3 = num1_int1 * num2_int2 + num1_int2 * num2_int1


        return str(prod1+prod2)+"+"+str(prod3)+"i"

