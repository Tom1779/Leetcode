def find_left(node, val, depth):
    if not node:
        return
    #if we are not deeper than max depth no need to store anything new
    depth += 1
    if depth > val[1]:
        val[1] = depth
        if node.left:
            val[0] = node.left.val
        else:
            val[0] = node.val
    find_left(node.left, val, depth)
    find_left(node.right, val, depth)
    


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        val = [root.val,0]

        find_left(root, val, 0)

        return val[0]