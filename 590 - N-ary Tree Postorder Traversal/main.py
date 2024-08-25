class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node'):
        def traverse(children, post_array):
            if children == []:
                return
            
            for node in children:
                if node.children != []:
                    traverse(node.children, post_array)
                post_array.append(node.val)
                
            
        if root == None:
            return []
        post_array = []
        
        traverse(root.children, post_array)
        post_array.append(root.val)
        
        return post_array