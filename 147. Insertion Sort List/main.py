# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        nodes =  []

        while(head):
            nodes.append(head)
            head = head.next

        for n in range(1,len(nodes)):
            for n2 in range(0,n):
                if nodes[n].val < nodes[n2].val:
                    temp = nodes[n]
                    nodes.pop(n)
                    nodes.insert(n2, temp)

        for n in range(len(nodes)-1):
            nodes[n].next = nodes[n+1]

        nodes[-1].next = None

        return nodes[0] 