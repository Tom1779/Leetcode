# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        nums = []
        self.getElements(nums, root1)
        self.getElements(nums, root2)

        return sorted(nums)


    def getElements(self, nums, node):
        if not node:
            return
        nums.append(node.val)
        self.getElements(nums, node.left)
        self.getElements(nums, node.right)