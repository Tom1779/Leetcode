# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        nodes = []

        while(head):
            nodes.append(head)
            head = head.next
        
        mid = (left + right) // 2

        for i in range(left - 1, mid):
            temp_val = nodes[i].val
            nodes[i].val = nodes[right - 1 - (i - (left-1))].val
            nodes[right - 1 - (i - (left-1))].val = temp_val

        return nodes[0]
