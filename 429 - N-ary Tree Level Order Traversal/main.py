"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

def getLevels(node, height, levels):
    if node == None:
        return

    height += 1
    if len(levels) < height:
        levels.append([node.val])
    else:
        levels[height-1].append(node.val)

    for n in node.children:
        getLevels(n, height, levels)

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = []

        getLevels(root, 0, levels)

        return levels