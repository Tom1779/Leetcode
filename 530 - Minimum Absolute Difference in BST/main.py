# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def create_val_list(node, val_list):
    if node == None:
        return
    val_list.append(node.val)
    create_val_list(node.left,val_list)
    create_val_list(node.right, val_list)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        val_list = []
        create_val_list(root, val_list)
        min_diff = 9999999
        val_list.sort()
        for val in range(len(val_list)-1):
            if  min_diff > (val_list[val+1] - val_list[val]):
                min_diff = (val_list[val+1] - val_list[val])
        return min_diff