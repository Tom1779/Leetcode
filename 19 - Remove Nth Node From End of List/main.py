# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_l = []
        temp = head
        while(temp):
            node_l.append(temp)
            temp = temp.next
        if(len(node_l) == 1):
            return None
        if(n < len(node_l) and n != 1):
            node_l[-n-1].next = node_l[-n+1]
        elif(n == len(node_l)):
            head = node_l[1]
        else:
            node_l[-2].next = None
            
        return head