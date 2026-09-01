# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        ordered = []
        connect = None
        temp1 = list1
        temp2 = list2
        while(temp1 != None or temp2 != None):
            if(temp1 != None):
                if(temp1.next == None):
                    connect = temp1
                ordered.append(temp1.val)
                temp1 = temp1.next
            if(temp2 != None):
                ordered.append(temp2.val)
                temp2 = temp2.next
                
        ordered.sort()
        connect.next = list2
        temp1 = list1
        count = 0
        while(temp1 != None):
            temp1.val = ordered[count]
            temp1 = temp1.next
            count += 1
            
        return list1
            
            
        