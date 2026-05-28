# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def build_tree(val, left, right):
    node = TreeNode(val)
    if len(left) > 0:
        left_indx = left.index(max(left))
        node.left = build_tree(left[left_indx], left[0:left_indx], left[left_indx+1:])
    if len(right) > 0:
        right_indx = right.index(max(right))
        node.right = build_tree(right[right_indx], right[0:right_indx], right[right_indx+1:])

    return node

    

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        val = max(nums)
        indx = nums.index(val)

        return build_tree(val, nums[0:indx], nums[indx+1:])