# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def get_deep_sum(node, cur_level, max_level, max_sum):
    if not node:
        return
    if cur_level == max_level[0]:
        max_sum[0] += node.val
    elif cur_level > max_level[0]:
        max_level[0] = cur_level
        max_sum[0] = node.val
    get_deep_sum(node.left, cur_level+1, max_level, max_sum)
    get_deep_sum(node.right, cur_level+1, max_level, max_sum)

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_level = [0]
        max_sum = [0]

        get_deep_sum(root, 1, max_level, max_sum)

        return max_sum[0]


