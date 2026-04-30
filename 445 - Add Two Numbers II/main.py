# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0

        while(l1):
            sum1 *= 10
            sum1 += l1.val
            l1 = l1.next

        while(l2):
            sum2 *= 10
            sum2 += l2.val
            l2 = l2.next

        total_sum = str(sum1+sum2)
        
        head = ListNode(int(total_sum[0]))
        tail = head
        for i in range(1, len(total_sum)):
            tail.next = ListNode(int(total_sum[i]))
            tail = tail.next

        return head