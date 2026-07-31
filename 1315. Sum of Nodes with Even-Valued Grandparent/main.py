# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def addgp(node, gp, p, total):
    if not node:
        return

    if gp and gp.val % 2 == 0:
        total[0] += node.val

    addgp(node.left, p, node, total)
    addgp(node.right, p, node, total)     


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        total = [0]

        addgp(root, None, None, total)

        return total[0]
        