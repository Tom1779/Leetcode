def createClone(node, clone_node, visited):
    if not node:
        return None

    if node in visited:
        return visited[node]

    visited[node] = clone_node

    for neighbor in node.neighbors:
        if neighbor in visited:
            clone_node.neighbors.append(visited[neighbor])
        else:
            clone_neighbor = Node(neighbor.val)
            clone_node.neighbors.append(clone_neighbor)
            createClone(neighbor, clone_neighbor, visited)

    return clone_node


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clone_node = Node(node.val)
        visited = {}

        return createClone(node, clone_node, visited)