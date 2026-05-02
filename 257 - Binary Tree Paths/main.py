# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def leaf_paths(node, paths, cur_path):
    cur_path = cur_path + str(node.val)
    if node.right == None and node.left == None:
        paths.append(cur_path)
        return
    if node.right:
        leaf_paths(node.right, paths, cur_path+"->")
    if node.left:
        leaf_paths(node.left, paths, cur_path+"->")

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        leaf_paths(root, paths, "")

        return paths