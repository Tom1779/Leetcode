# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def count_nodes(node, count):
    if node == None:
        return
    count[0] += 1
    count_nodes(node.left, count)
    count_nodes(node.right, count)


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = [0]

        count_nodes(root, count)

        return count[0]