# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def tree_leaf_sum(node, total, cur_total):
    cur_total *= 10
    cur_total += node.val
    #leaf node
    if node.right == None and node.left == None:
        total[0] += cur_total
        return
    if node.left:
        tree_leaf_sum(node.left, total, cur_total)
    if node.right:
        tree_leaf_sum(node.right, total, cur_total)

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #stroing total in list so we can access it at any point and value changes between left and right recursion
        total = [0]

        tree_leaf_sum(root, total, 0)

        return total[0]