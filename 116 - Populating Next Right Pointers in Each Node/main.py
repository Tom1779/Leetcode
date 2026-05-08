"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
def get_next(node, levels, current_level):
    if not node:
        return
    if not current_level in levels:
        levels[current_level] = [node]
    else:
        levels[current_level][-1].next = node
        levels[current_level].append(node)

    get_next(node.left, levels, current_level+1)
    get_next(node.right, levels, current_level+1)

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
        
        levels = dict()
        get_next(root, levels, 0)

        return root
