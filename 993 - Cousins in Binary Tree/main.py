# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def get_nodes(parents, parent, node, x, y, level, levels):
    if not node:
        return
    if node.val == x:
        levels[0] = level
        parents[0] = parent
        if levels[1] != -1:
            return
    if node.val == y:
        levels[1] = level
        parents[1] = parent
        if levels[0] != -1:
            return

    get_nodes(parents, node, node.left, x, y, level+1, levels)
    get_nodes(parents, node, node.right, x, y, level+1, levels)
    
    



class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        levels = [-1,-1]
        parents = [None, None]

        get_nodes(parents, None, root, x, y, 0, levels)

        if levels[0] == levels[1] and parents[0] != parents[1]:
            return True

        return False