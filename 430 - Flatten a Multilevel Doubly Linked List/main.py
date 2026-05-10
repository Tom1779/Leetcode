"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
def flatten_list(nodes, node, temp_next):
    nodes.append(node)
    if node.child != None:
        if node.next:
            temp_next.append(node.next)
        node.next = node.child
        node.next.prev = node
        node.child = None
        flatten_list(nodes, node.next, temp_next)
    elif node.next == None:
        if len(temp_next) > 0:
            node.next = temp_next.pop()
            node.next.prev = node
            flatten_list(nodes, node.next, temp_next)
        return
    else:
        flatten_list(nodes, node.next, temp_next)


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        nodes = []

        flatten_list(nodes, head, [])

        return nodes[0]