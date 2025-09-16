# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def invertnodes(head):
    if head.right == None and head.left == None:
        return
    temp = head.right
    head.right = head.left
    head.left = temp
    if head.right:
        invertnodes(head.right)
    if head.left:
        invertnodes(head.left)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        invertnodes(root)

        return root