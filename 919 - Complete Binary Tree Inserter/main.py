# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root                

    def search_for_insert(self, node, level, ins_node):
        if not node.left or not node.right:
            if level < ins_node[1]:
                ins_node[0] = node
                ins_node[1] = level
            return
        self.search_for_insert(node.left, level+1, ins_node)
        self.search_for_insert(node.right, level+1, ins_node)

    def insert(self, val: int) -> int:
        ins_node = [None, 99999999999999]
        self.search_for_insert(self.root, 0, ins_node)
        node = TreeNode(val)
        if ins_node[0] == None:
            temp = self.root
            while(temp.left):
                temp = temp.left
            temp.left = node
            return temp.val
        if ins_node[0].left == None:
            ins_node[0].left = node
        else:
            ins_node[0].right = node
        return ins_node[0].val


    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()