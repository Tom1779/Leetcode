# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def get_sums(node, curSum, target, allSums):
            if node == None:
                return
            curSum.append(node.val)
            temp = list(curSum)
            if sum(curSum) == target and node.right == None and node.left == None:
                allSums.append(curSum)
            get_sums(node.right, curSum, target, allSums)
            get_sums(node.left, temp, target, allSums)
            
        allSums = []
        get_sums(root, [], targetSum, allSums)
        
        return allSums