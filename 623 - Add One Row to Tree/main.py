def addRow(cur_depth, depth, node, val):
    if cur_depth + 1 == depth:
        left_node = TreeNode(val)
        right_node = TreeNode(val)

        left_node.left = node.left
        right_node.right = node.right

        node.left = left_node
        node.right = right_node
        return

    if node.left:
        addRow(cur_depth + 1, depth, node.left, val)

    if node.right:
        addRow(cur_depth + 1, depth, node.right, val)


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        addRow(1, depth, root, val)

        return root