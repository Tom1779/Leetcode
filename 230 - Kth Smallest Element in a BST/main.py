# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def add_value(node, values):
    if node == None:
        return
    values.append(node.val)
    add_value(node.left, values)
    add_value(node.right, values)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        add_value(root, values)

        values.sort()

        return values[k-1]