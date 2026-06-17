# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def get_avg(level, sums, node):
    if None == node:
        return
    if level in sums:
        sums[level][0] += 1
        sums[level][1] += node.val
    else:
        sums[level] = [1, node.val]
        
    get_avg(level+1, sums, node.left)
    get_avg(level+1, sums, node.right)

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sums = dict()

        get_avg(0, sums, root)

        return [a[1]/a[0] for a in sums.values()]
