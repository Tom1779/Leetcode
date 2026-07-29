# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def findNode(val, node):
    if not node:
        return
    if node.val == val:
        return node
    is_found = findNode(val, node.left)
    if is_found:
        return is_found
    return findNode(val, node.right)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        return findNode(val, root)