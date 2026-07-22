# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        index_dict = dict()

        for num in range(len(nums)):
            index_dict[nums[num]] = num

        total = 0
        prev = -1

        while(head):
            if not head.val in index_dict:
                if prev in index_dict:
                    total += 1
            prev = head.val
            head = head.next

        if prev in index_dict:
            total += 1
        
        return total