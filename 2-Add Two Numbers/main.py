class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = []
        num2 = []
        while(l1 != None):
            num1.insert(0, str(l1.val))
            l1 = l1.next
        while(l2 != None):
            num2.insert(0, str(l2.val))
            l2 = l2.next
        
        num1 = int("".join(num1))
        num2 = int("".join(num2))
        
        total = str(num1+num2)
        head = ListNode(int(total[-1]))
        total = total[:-1]
        temp = head
        for digit in total[::-1]:
            newNode = ListNode(int(digit))
            temp.next = newNode
            temp = temp.next
            
        return head