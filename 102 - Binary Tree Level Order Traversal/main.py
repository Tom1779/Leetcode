# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def getLevels(node, level, levels):
    if not node:
        return
    if level == len(levels):
        levels.append([node.val])
    else:
        levels[level].append(node.val)
    getLevels(node.left, level+1, levels)
    getLevels(node.right, level+1, levels)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        getLevels(root, 0, levels)

        return levels
        