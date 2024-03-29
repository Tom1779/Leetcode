# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        node_set = set()
        while(head != None):
            if(head in node_set):
                return head
            node_set.add(head)
            head = head.next