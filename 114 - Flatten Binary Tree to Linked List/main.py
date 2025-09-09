# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def flatten_tree(node, flat_list):
    if node == None:
        return
    flat_list.append(node)
    flatten_tree(node.left, flat_list)
    flatten_tree(node.right, flat_list)

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        flat_list = []
        flatten_tree(root, flat_list)

        for node in range(len(flat_list)-1):
            flat_list[node].left = None
            flat_list[node].right = flat_list[node+1]