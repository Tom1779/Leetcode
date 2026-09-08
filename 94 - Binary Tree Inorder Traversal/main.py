# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(self, node, l):
            if node == None:
                return
            inorder(self, node.left, l)
            l.append(node.val)
            inorder(self, node.right, l)
            
        l = []
        
        inorder(self, root, l)
        
        return l
        